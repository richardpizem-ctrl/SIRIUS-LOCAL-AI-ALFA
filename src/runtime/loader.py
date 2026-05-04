import os
import json
import importlib.util
import logging
import time

log = logging.getLogger(__name__)


class PluginLoader:
    """
    PluginLoader 4.0
    - Loads plugins from /plugins
    - Validates manifest.json
    - Imports plugin.py safely
    - Supports dependencies
    - Security Family integration
    - Plugin lifecycle (load → init → register → start)
    - Error isolation
    - Telemetry
    """

    def __init__(self, plugins_dir: str = "plugins"):
        self.plugins_dir = plugins_dir
        self.instances = {}
        self.metadata = {}

    # --------------------------------------------------------
    # PUBLIC API
    # --------------------------------------------------------
    def load_all(self, runtime_manager):
        if not os.path.exists(self.plugins_dir):
            log.warning("Plugins directory not found: %s", self.plugins_dir)
            return

        # First pass: load manifests
        manifests = self._load_all_manifests()

        # Resolve dependencies
        order = self._resolve_dependencies(manifests)

        # Load plugins in dependency order
        for name in order:
            manifest = manifests[name]
            instance = self._load_single_plugin(manifest, runtime_manager)

            if instance:
                self.instances[name] = instance
                self.metadata[name] = manifest
                log.info("Plugin loaded: %s", name)

        # Start plugins
        for name, instance in self.instances.items():
            try:
                if hasattr(instance, "start"):
                    instance.start()
                log.info("Plugin started: %s", name)
            except Exception as exc:
                log.exception("Failed to start plugin '%s': %s", name, exc)

    # --------------------------------------------------------
    # LOAD ALL MANIFESTS
    # --------------------------------------------------------
    def _load_all_manifests(self):
        manifests = {}

        for folder in os.listdir(self.plugins_dir):
            plugin_path = os.path.join(self.plugins_dir, folder)
            if not os.path.isdir(plugin_path):
                continue

            manifest_path = os.path.join(plugin_path, "manifest.json")
            if not os.path.exists(manifest_path):
                log.warning("Missing manifest.json in %s", plugin_path)
                continue

            manifest = self._load_manifest(manifest_path)
            if not manifest:
                continue

            name = manifest.get("name")
            if not name:
                log.error("Manifest missing 'name' in %s", manifest_path)
                continue

            manifests[name] = manifest

        return manifests

    # --------------------------------------------------------
    # DEPENDENCY RESOLUTION
    # --------------------------------------------------------
    def _resolve_dependencies(self, manifests: dict):
        resolved = []
        unresolved = set(manifests.keys())

        while unresolved:
            progress = False

            for name in list(unresolved):
                deps = manifests[name].get("depends_on", [])

                if all(d in resolved for d in deps):
                    resolved.append(name)
                    unresolved.remove(name)
                    progress = True

            if not progress:
                raise RuntimeError("Circular or unresolved plugin dependencies.")

        log.info("Plugin load order: %s", resolved)
        return resolved

    # --------------------------------------------------------
    # LOAD SINGLE PLUGIN
    # --------------------------------------------------------
    def _load_single_plugin(self, manifest: dict, runtime_manager):
        name = manifest.get("name")
        plugin_dir = os.path.join(self.plugins_dir, name)
        plugin_file = os.path.join(plugin_dir, "plugin.py")

        if not manifest.get("enabled", True):
            log.info("Plugin disabled: %s", name)
            return None

        if not os.path.exists(plugin_file):
            log.error("Missing plugin.py for plugin '%s'", name)
            return None

        # Security Family: risk check
        risk = manifest.get("risk_level", 0)
        if risk > runtime_manager.security.max_plugin_risk:
            log.warning("Plugin '%s' blocked due to high risk.", name)
            return None

        # Import plugin
        instance = self._import_plugin(plugin_file, manifest)
        if not instance:
            return None

        # Initialize plugin
        try:
            if hasattr(instance, "initialize"):
                instance.initialize(runtime_manager)
        except Exception as exc:
            log.exception("Failed to initialize plugin '%s': %s", name, exc)
            return None

        # Register plugin
        try:
            if hasattr(instance, "register"):
                instance.register(runtime_manager)
        except Exception as exc:
            log.exception("Failed to register plugin '%s': %s", name, exc)
            return None

        return instance

    # --------------------------------------------------------
    # MANIFEST LOADING
    # --------------------------------------------------------
    def _load_manifest(self, path: str):
        try:
            with open(path, "r", encoding="utf-8") as f:
                manifest = json.load(f)

            # Basic validation
            if "name" not in manifest:
                raise ValueError("Manifest missing 'name'")

            return manifest

        except Exception as e:
            log.exception("Failed to load manifest %s: %s", path, e)
            return None

    # --------------------------------------------------------
    # IMPORT PLUGIN
    # --------------------------------------------------------
    def _import_plugin(self, plugin_file: str, manifest: dict):
        try:
            spec = importlib.util.spec_from_file_location(
                manifest["name"], plugin_file
            )
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)

            if not hasattr(module, "Plugin"):
                log.error("Plugin class missing in %s", plugin_file)
                return None

            cls = module.Plugin

            if not callable(cls):
                log.error("Plugin is not a class in %s", plugin_file)
                return None

            return cls(manifest)

        except Exception as e:
            log.exception("PluginLoader error in %s: %s", plugin_file, e)
            return None
