import json
import os
import copy
from datetime import datetime

# NEW BACKEND MODULES
from email.email_storage import EmailStorage
from email.email_validator import EmailValidator
from email.email_renderer import EmailRenderer
from email.email_profile_manager import EmailProfileManager


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
    - validate email fields
    - render previews and exports
    """

    def __init__(self, base_path="emails", profile_path="email_profiles"):
        self.base_path = base_path
        self.profile_path = profile_path

        os.makedirs(self.base_path, exist_ok=True)
        os.makedirs(self.profile_path, exist_ok=True)

        # BACKEND MODULES
        self.storage = EmailStorage(base_path=self.base_path)
        self.validator = EmailValidator()
        self.renderer = EmailRenderer()
        self.profile_manager = EmailProfileManager(base_path=self.profile_path)

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

        # VALIDATION
        validation = self.validator.validate_full(to, subject, body)
        if not validation["all_valid"]:
            return {
                "status": "error",
                "message": "Validation failed.",
                "details": validation
            }

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

        self.storage.save(draft, prefix="draft")
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

        self.storage.save(sent, prefix="sent")
        return sent

    # ============================================================
    #  LIST EMAILS
    # ============================================================

    def list_emails(self, status=None):
        return self.storage.list(status=status)

    # ============================================================
    #  LOAD EMAIL
    # ============================================================

    def load_email(self, email_id: str):
        return self.storage.load(email_id)

    # ============================================================
    #  DELETE EMAIL
    # ============================================================

    def delete_email(self, email_id: str):
        return self.storage.delete(email_id)

    # ============================================================
    #  PROFILE MANAGEMENT
    # ============================================================

    def save_profile(self, name: str, profile: dict):
        return self.profile_manager.save_profile(name, profile)

    def load_profile(self, name: str):
        return self.profile_manager.load_profile(name)

    def list_profiles(self):
        return self.profile_manager.list_profiles()

    def delete_profile(self, name: str):
        return self.profile_manager.delete_profile(name)

    # ============================================================
    #  RENDERING
    # ============================================================

    def render_preview(self, email: dict):
        return self.renderer.render_preview(email)

    def render_full(self, email: dict):
        return self.renderer.render_full(email)

    def render_export(self, email: dict):
        return self.renderer.render_export(email)
