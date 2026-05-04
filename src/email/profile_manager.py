import os
import json


class EmailProfileManager:
    """
    EmailProfileManager 4.0
    Handles creation, loading, listing, and deletion of
    email sender profiles.

    Used internally by EmailManager and email-profile command.
    """

    def __init__(self, base_path="email_profiles"):
        self.base_path = base_path
        os.makedirs(self.base_path, exist_ok=True)

    # ---------------------------------------------------------
    # PATH HELPERS
    # ---------------------------------------------------------
    def _path(self, name: str):
        return os.path.join(self.base_path, f"{name}.json")

    def _exists(self, name: str):
        return os.path.isfile(self._path(name))

    # ---------------------------------------------------------
    # SAVE PROFILE
    # ---------------------------------------------------------
    def save_profile(self, name: str, profile: dict):
        """
        Saves a profile to disk.
        """
        with open(self._path(name), "w", encoding="utf-8") as f:
            json.dump(profile, f, indent=2, ensure_ascii=False)
        return True

    # ---------------------------------------------------------
    # LOAD PROFILE
    # ---------------------------------------------------------
    def load_profile(self, name: str):
        """
        Loads a profile by name.
        """
        if not self._exists(name):
            return None

        with open(self._path(name), "r", encoding="utf-8") as f:
            return json.load(f)

    # ---------------------------------------------------------
    # LIST PROFILES
    # ---------------------------------------------------------
    def list_profiles(self):
        """
        Returns a list of all profile names.
        """
        profiles = []
        for f in os.listdir(self.base_path):
            if f.endswith(".json"):
                profiles.append(f.replace(".json", ""))
        return profiles

    # ---------------------------------------------------------
    # DELETE PROFILE
    # ---------------------------------------------------------
    def delete_profile(self, name: str):
        """
        Deletes a profile by name.
        """
        if not self._exists(name):
            return False

        os.remove(self._path(name))
        return True
