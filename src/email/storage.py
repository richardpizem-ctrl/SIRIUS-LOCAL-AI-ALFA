import os
import json
from datetime import datetime


class EmailStorage:
    """
    EmailStorage 4.0
    Handles low-level file operations for storing, loading,
    listing, and deleting emails.

    This module is used internally by EmailManager.
    """

    def __init__(self, base_path="emails"):
        self.base_path = base_path
        os.makedirs(self.base_path, exist_ok=True)

    # ---------------------------------------------------------
    # PATH HELPERS
    # ---------------------------------------------------------
    def _path(self, filename: str):
        return os.path.join(self.base_path, filename)

    # ---------------------------------------------------------
    # SAVE EMAIL
    # ---------------------------------------------------------
    def save(self, email_data: dict, prefix: str):
        """
        Saves an email (draft or sent) with a prefix:
        draft_20260504_120000.json
        sent_20260504_120000.json
        """
        email_id = email_data.get("id")
        filename = f"{prefix}_{email_id}.json"

        with open(self._path(filename), "w", encoding="utf-8") as f:
            json.dump(email_data, f, indent=2, ensure_ascii=False)

        return filename

    # ---------------------------------------------------------
    # LOAD EMAIL BY ID
    # ---------------------------------------------------------
    def load(self, email_id: str):
        """
        Loads an email by ID, regardless of prefix.
        """
        for f in os.listdir(self.base_path):
            if f.endswith(".json") and email_id in f:
                with open(self._path(f), "r", encoding="utf-8") as file:
                    return json.load(file)
        return None

    # ---------------------------------------------------------
    # LIST EMAILS
    # ---------------------------------------------------------
    def list(self, status=None):
        """
        Lists all emails or filters by status (draft/sent).
        """
        emails = []

        for f in os.listdir(self.base_path):
            if not f.endswith(".json"):
                continue

            with open(self._path(f), "r", encoding="utf-8") as file:
                data = json.load(file)

            if status is None or data.get("status") == status:
                emails.append(data)

        return emails

    # ---------------------------------------------------------
    # DELETE EMAIL
    # ---------------------------------------------------------
    def delete(self, email_id: str):
        """
        Deletes an email by ID.
        """
        for f in os.listdir(self.base_path):
            if f.endswith(".json") and email_id in f:
                os.remove(self._path(f))
                return True
        return False
