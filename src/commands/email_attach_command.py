from commands.base_command import BaseCommand
from email.manager import EmailManager
import os


class EmailAttachCommand(BaseCommand):
    """
    EmailAttachCommand 4.0
    Adds an attachment to an existing email draft.
    """

    name = "email-attach"
    description = "Adds an attachment to an email draft."
    category = "email"

    required_identity = "OWNER"
    risk_level = 0.6
    capabilities = ["fs_read", "fs_write"]

    keywords = ["email", "attach", "file", "draft"]
    examples = ["email-attach 20260424_112233 ./docs/file.pdf"]

    def __init__(self, context, email_manager: EmailManager):
        self.context = context
        self.email_manager = email_manager

    def execute(self, *args, **kwargs):
        if len(args) < 2:
            return {
                "status": "error",
                "message": "Usage: email-attach <draft_id> <file_path>"
            }

        draft_id = args[0]
        file_path = args[1]

        # -----------------------------
        # CHECK FILE EXISTS
        # -----------------------------
        if not os.path.isfile(file_path):
            return {
                "status": "error",
                "message": f"File '{file_path}' does not exist."
            }

        # -----------------------------
        # VALIDATE ATTACHMENT PATH
        # -----------------------------
        if not self.email_manager.validator.validate_attachment(file_path):
            return {
                "status": "error",
                "message": "Invalid attachment path."
            }

        # -----------------------------
        # LOAD DRAFT
        # -----------------------------
        draft = self.email_manager.load_email(draft_id)
        if draft is None:
            return {
                "status": "error",
                "message": f"Draft '{draft_id}' not found."
            }

        if draft.get("status") != "draft":
            return {
                "status": "error",
                "message": f"Email '{draft_id}' is not a draft."
            }

        # -----------------------------
        # SNAPSHOT BEFORE MODIFYING
        # -----------------------------
        if hasattr(self.context, "snapshot"):
            self.context.snapshot()

        # -----------------------------
        # ADD ATTACHMENT
        # -----------------------------
        attachments = draft.get("attachments", [])
        attachments.append(file_path)
        draft["attachments"] = attachments

        # -----------------------------
        # SAVE UPDATED DRAFT (via storage)
        # -----------------------------
        self.email_manager.storage.save(draft, prefix="draft")

        # -----------------------------
        # LOG INTO CONTEXT STATE
        # -----------------------------
        self.context.merge({
            "last_email_attachment_added": file_path,
            "last_email_attachment_draft": draft_id
        })

        return {
            "status": "success",
            "message": "Attachment added successfully.",
            "draft_id": draft_id,
            "file": file_path,
            "attachment_count": len(attachments)
        }
