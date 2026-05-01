import os
import json
import importlib.util
from typing import List
from .runtime_manager import RuntimeManager

_runtime = None


# ============================================================
# PLUGINLOADER 2.0
# ============================================================

class PluginLoader:
    """
    PluginLoader 2.0
    - načítava pluginy z priečinka /plugins
    - číta manifest.json
    - importuje plugin.py
    - vytvára inštancie pluginov
    - poskytuje RuntimeManageru zoznam pluginov
    """

    def __init__(self, plugins_dir: str = "plugins"):
        self.plugins_dir = plugins_dir
        self.instances = []  # zoznam inštancií pluginov

    # --------------------------------------------------------
    # PUBLIC API
    # --------------------------------------------------------
    def load_all(self):
        """
        Načíta všetky pluginy z priečinka plugins/.
        """
        if not os.path.exists(self.plugins_dir):
            return

        for folder in os.listdir(self.plugins_dir):
            plugin_path = os.path.join(self.plugins_dir, folder)

            if not os.path.isdir(plugin_path):
                continue

            manifest_path = os.path.join(plugin_path, "manifest.json")
            plugin_file = os.path.join(plugin_path, "plugin.py")

            # manifest musí existovať
            if not os.path.exists(manifest_path):
                continue

            # načítanie manifestu
            manifest = self._load_manifest(manifest_path)
            if not manifest:
                continue

            # plugin musí byť enabled
            if not manifest.get("enabled", True):
                continue

            # plugin.py musí existovať
            if not os.path.exists(plugin_file):
                continue

            # import pluginu
            instance = self._import_plugin(plugin_file, manifest)
            if instance:
                self.instances.append(instance)

    # --------------------------------------------------------
    # INTERNAL HELPERS
    # --------------------------------------------------------
    def _load_manifest(self, path: str):
        try:
            with open(path, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return None

    def _import_plugin(self, plugin_file: str, manifest: dict):
        """
        Dynamicky importuje plugin.py a vytvorí inštanciu triedy Plugin.
        """
        try:
            spec = importlib.util.spec_from_file_location(
                manifest["name"], plugin_file
            )
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)

            if not hasattr(module, "Plugin"):
                return None

            # vytvorenie inštancie pluginu
            return module.Plugin

        except Exception as e:
            print(f"PluginLoader error: {e}")
            return None


# ============================================================
# RUNTIME BOOTSTRAP
# ============================================================

def get_runtime():
    """
    Globálny runtime bootstrapper.
    Vytvorí RuntimeManager iba raz a zdieľa ho v celom systéme.
    """
    global _runtime
    if _runtime is None:
        _runtime = RuntimeManager()
        _runtime.initialize()
    return _runtime
