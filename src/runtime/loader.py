import os
import json
import importlib.util
import logging

log = logging.getLogger(__name__)


class PluginLoader:
    """
    PluginLoader 2.0
    - načítava pluginy z priečinka /plugins
    - číta manifest.json
    - importuje plugin.py
    - vytvára inštancie pluginov
    - registruje ich do RuntimeManagera
    """

    def __init__(self, plugins_dir: str = "plugins"):
        self.plugins_dir = plugins_dir
        self.instances = []

    # --------------------------------------------------------
    # PUBLIC API
    # --------------------------------------------------------
    def load_all(self, runtime_manager):
        if not os.path.exists(self.plugins_dir):
            log.warning("Plugins directory not found: %s", self.plugins_dir)
            return

        for folder in os.listdir(self.plugins_dir):
            plugin_path = os.path.join(self.plugins_dir, folder)

            if not os.path.isdir(plugin_path):
                continue

            manifest_path = os.path.join(plugin_path, "manifest.json")
            plugin_file = os.path.join(plugin_path, "plugin.py")

            if not os.path.exists(manifest_path):
                log.warning("Missing manifest.json in %s", plugin_path)
                continue

            manifest = self._load_manifest(manifest_path)
            if not manifest:
                log.error("Invalid manifest in %s", plugin_path)
                continue

            if not manifest.get("enabled", True):
                log.info("Plugin disabled: %s", manifest.get("name"))
                continue

            if not os.path.exists(plugin_file):
                log.error("Missing plugin.py in %s", plugin_path)
                continue

            instance = self._import_plugin(plugin_file, manifest)
            if not instance:
                continue

            # registrácia pluginu do runtime
            if hasattr(instance, "register"):
                instance.register(runtime_manager)

            self.instances.append(instance)
            log.info("Plugin loaded: %s", manifest.get("name"))

    # --------------------------------------------------------
    # INTERNAL HELPERS
    # --------------------------------------------------------
    def _load_manifest(self, path: str):
        try:
            with open(path, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception as e:
            log.exception("Failed to load manifest %s: %s", path, e)
            return None

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
