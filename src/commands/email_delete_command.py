from commands.base_command import BaseCommand
from email.manager import EmailManager


class EmailDeleteCommand(BaseCommand):
    """
    EmailDeleteCommand 4.0
    Deletes an email (draft or sent) by ID using EmailManager.

    New in v4.0:
    - NL Router metadata
    - SECURITY FAMILY enforcement
    - OWNER-only execution
    - structured JSON output
    - safe deletion pipeline
    """

    # ---------------------------------------------------------
    # METADATA (v4.0)
    # ---------------------------------------------------------
    name = "email-delete"
    description = "Deletes an email draft or sent email by ID."
    category = "email"

    required_identity = "OWNER"     # Only OWNER can delete emails
    risk_level = 0.5                # Medium risk (destructive action)
    capabilities = ["fs_write"]

    keywords = ["email", "delete", "remove"]
    examples = ["email-delete 20260424_112233"]

    # ---------------------------------------------------------
    # INIT
    # ---------------------------------------------------------
    def __init__(self, context, email_manager: EmailManager):
        self.context = context
        self.email_manager = email_manager

    # ---------------------------------------------------------
    # EXECUTION
    # ---------------------------------------------------------
    def execute(self, *args, **kwargs):
        """
        Deletes an email by ID.
        Usage:
            email-delete <email_id>
        """

        # -----------------------------
        # INPUT VALIDATION
        # -----------------------------
        if len(args) < 1:
            return {
                "status": "error",
                "message": "Usage: email-delete <email_id>"
            }

        email_id = args[0]

        # -----------------------------
        # SNAPSHOT BEFORE DELETE
        # -----------------------------
        if hasattr(self.context, "snapshot"):
            self.context.snapshot()

        # -----------------------------
        # DELETE EMAIL
        # -----------------------------
        success = self.email_manager.delete_email(email_id)

        if not success:
            return {
                "status": "error",
                "message": f"Email '{email_id}' not found."
            }

        # -----------------------------
        # LOG INTO CONTEXT STATE
        # -----------------------------
        self.context.merge({
            "last_email_deleted_id": email_id
        })

        # -----------------------------
        # SUCCESS RESPONSE
        # -----------------------------
        return {
            "status": "success",
            "message": f"Email '{email_id}' deleted successfully.",
            "email_id": email_id
        }
