import json
import os
import copy
from datetime import datetime


class EmailManager:
    """
    EmailManager 4.0
    Core orchestrator for the Email Engine in SIRIUS LOCAL AI.

    Responsibilities:
    - create email drafts
    - send emails (placeholder)
    - store emails locally
    - manage attachments
    - manage sender profiles
    - provide structured metadata for commands

    This module is intentionally backend‑only.
    Commands (email-send, email-draft, etc.) will call this manager.
    """

    def __init__(self, base_path="emails", profile_path="email_profiles"):
        self.base_path = base_path
        self.profile_path = profile_path

        os.makedirs(self.base_path, exist_ok=True)
        os.makedirs(self.profile_path, exist_ok=True)

    # ============================================================
    #  INTERNAL HELPERS
    # ============================================================

    def _email_path(self, filename: str):
        return os.path.join(self.base_path, filename)

    def _profile_path(self, name: str):
        return os.path.join(self.profile_path, f"{name}.json")

    # ============================================================
    #  DRAFT CREATION
    # ============================================================

    def create_draft(self, to: str, subject: str, body: str, attachments=None):
        """
        Creates a new email draft and stores it locally.
        """
        attachments = attachments or []

        draft = {
            "id": datetime.now().strftime("%Y%m%d_%H%M%S"),
            "to": to,
            "subject": subject,
            "body": body,
            "attachments": attachments,
            "created_at": datetime.now().isoformat(),
            "status": "draft"
        }

        filename = f"draft_{draft['id']}.json"

        with open(self._email_path(filename), "w", encoding="utf-8") as f:
            json.dump(draft, f, indent=2, ensure_ascii=False)

        return draft

    # ============================================================
    #  SEND EMAIL (PLACEHOLDER)
    # ============================================================

    def send_email(self, draft: dict, sender_profile: dict | None = None):
        """
        Placeholder email sending logic.
        In real implementation, this would integrate with SMTP or API.
        """

        sent = copy.deepcopy(draft)
        sent["status"] = "sent"
        sent["sent_at"] = datetime.now().isoformat()
        sent["sender_profile"] = sender_profile or {}

        filename = f"sent_{sent['id']}.json"

        with open(self._email_path(filename), "w", encoding="utf-8") as f:
            json.dump(sent, f, indent=2, ensure_ascii=False)

        return sent

    # ============================================================
    #  LIST EMAILS
    # ============================================================

    def list_emails(self, status=None):
        """
        Lists all emails or filters by status (draft/sent).
        """
        files = os.listdir(self.base_path)
        emails = []

        for f in files:
            if not f.endswith(".json"):
                continue

            with open(self._email_path(f), "r", encoding="utf-8") as file:
                data = json.load(file)

            if status is None or data.get("status") == status:
                emails.append(data)

        return emails

    # ============================================================
    #  LOAD EMAIL
    # ============================================================

    def load_email(self, email_id: str):
        """
        Loads a draft or sent email by ID.
        """
        for f in os.listdir(self.base_path):
            if f.endswith(".json") and email_id in f:
                with open(self._email_path(f), "r", encoding="utf-8") as file:
                    return json.load(file)
        return None

    # ============================================================
    #  DELETE EMAIL
    # ============================================================

    def delete_email(self, email_id: str):
        """
        Deletes an email by ID.
        """
        for f in os.listdir(self.base_path):
            if f.endswith(".json") and email_id in f:
                os.remove(self._email_path(f))
                return True
        return False

    # ============================================================
    #  PROFILE MANAGEMENT
    # ============================================================

    def save_profile(self, name: str, profile: dict):
        """
        Saves a sender profile.
        """
        with open(self._profile_path(name), "w", encoding="utf-8") as f:
            json.dump(profile, f, indent=2, ensure_ascii=False)
        return True

    def load_profile(self, name: str):
        """
        Loads a sender profile.
        """
        path = self._profile_path(name)
        if not os.path.isfile(path):
            return None

        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)

    def list_profiles(self):
        """
        Lists all sender profiles.
        """
        files = os.listdir(self.profile_path)
        return [f.replace(".json", "") for f in files if f.endswith(".json")]

    def delete_profile(self, name: str):
        """
        Deletes a sender profile.
        """
        path = self._profile_path(name)
        if os.path.isfile(path):
            os.remove(path)
            return True
        return False
