import copy
import os
import json
import re


class ProfileManager:
    """
    Spravuje profily kontextu.
    """

    VALID_NAME = re.compile(r"^[A-Za-z0-9_\-]+$")

    def __init__(self, context_manager, base_path="profiles"):
        self.context = context_manager
        self.base_path = base_path

        if not os.path.exists(self.base_path):
            os.makedirs(self.base_path)

    # ============================================================
    #  POMOCNÉ FUNKCIE
    # ============================================================

    def _profile_path(self, name: str):
        return os.path.join(self.base_path, f"{name}.json")

    def _exists(self, name: str):
        return os.path.isfile(self._profile_path(name))

    def _validate_name(self, name: str):
        return bool(self.VALID_NAME.match(name))

    # ============================================================
    #  ULOŽENIE PROFILU
    # ============================================================

    def save_profile(self, name: str):
        if not self._validate_name(name):
            return False

        data = {
            "session": copy.deepcopy(self.context.session_memory),
            "persistent": copy.deepcopy(self.context.persistent_memory),
            "state": copy.deepcopy(self.context.state),
            "history": copy.deepcopy(self.context.history),
        }

        with open(self._profile_path(name), "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

        return True

    # ============================================================
    #  NAČÍTANIE PROFILU
    # ============================================================

    def load_profile(self, name: str):
        if not self._exists(name):
            return None

        with open(self._profile_path(name), "r", encoding="utf-8") as f:
            data = json.load(f)

        # Validácia JSON štruktúry
        if not isinstance(data, dict):
            return None

        session = data.get("session", [])
        persistent = data.get("persistent", {})
        state = data.get("state", {})
        history = data.get("history", [])

        if not isinstance(session, list):
            return None
        if not isinstance(persistent, dict):
            return None
        if not isinstance(state, dict):
            return None
        if not isinstance(history, list):
            return None

        # Obnova kontextu (deep copy)
        self.context.session_memory = copy.deepcopy(session)
        self.context.persistent_memory = copy.deepcopy(persistent)
        self.context.state = copy.deepcopy(state)

        # rešpektovať max_history
        self.context.history = copy.deepcopy(history[-self.context.max_history:])

        return True

    # ============================================================
    #  ZOZNAM PROFILOV
    # ============================================================

    def list_profiles(self):
        files = os.listdir(self.base_path)
        profiles = [f.replace(".json", "") for f in files if f.endswith(".json")]
        return profiles

    # ============================================================
    #  ZMAZANIE PROFILU
    # ============================================================

    def delete_profile(self, name: str):
        if not self._exists(name):
            return False

        os.remove(self._profile_path(name))
        return True

    # ============================================================
    #  INFO O PROFILE
    # ============================================================

    def get_profile_info(self, name: str):
        if not self._exists(name):
            return None

        with open(self._profile_path(name), "r", encoding="utf-8") as f:
            data = json.load(f)

        return {
            "session_items": len(data.get("session", [])),
            "persistent_items": len(data.get("persistent", {})),
            "state_items": len(data.get("state", {})),
            "history_snapshots": len(data.get("history", [])),
        }
