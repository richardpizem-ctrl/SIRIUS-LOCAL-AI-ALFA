from commands.base_command import BaseCommand
from email.manager import EmailManager


class EmailSendCommand(BaseCommand):
    """
    EmailSendCommand 4.0
    Sends an email using EmailManager with validation, snapshot,
    profile loading, and structured JSON output.
    """

    # ---------------------------------------------------------
    # METADATA (v4.0)
    # ---------------------------------------------------------
    name = "email-send"
    description = "Sends an email using EmailManager."
    category = "email"

    required_identity = "OWNER"
    risk_level = 0.8
    capabilities = ["context_read", "context_write", "fs_read", "fs_write"]

    keywords = ["email", "send", "mail"]
    examples = ["email-send profile_name draft_id"]

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
        Sends an email using a draft ID and a sender profile.
        Usage:
            email-send <profile> <draft_id>
        """

        # -----------------------------
        # INPUT VALIDATION
        # -----------------------------
        if len(args) < 2:
            return {
                "status": "error",
                "message": "Usage: email-send <profile> <draft_id>"
            }

        profile_name = args[0]
        draft_id = args[1]

        # -----------------------------
        # LOAD PROFILE
        # -----------------------------
        profile = self.email_manager.load_profile(profile_name)
        if profile is None:
            return {
                "status": "error",
                "message": f"Profile '{profile_name}' does not exist."
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
        # SNAPSHOT BEFORE SENDING
        # -----------------------------
        if hasattr(self.context, "snapshot"):
            self.context.snapshot()

        # -----------------------------
        # SEND EMAIL
        # -----------------------------
        sent_email = self.email_manager.send_email(draft, profile)

        # Extract actual email object
        email = sent_email["email"]

        # -----------------------------
        # LOG INTO CONTEXT STATE
        # -----------------------------
        self.context.merge({
            "last_email_sent_id": email["id"],
            "last_email_sent_to": email["to"],
            "last_email_sent_subject": email["subject"]
        })

        # -----------------------------
        # SUCCESS RESPONSE
        # -----------------------------
        return {
            "status": "success",
            "message": "Email sent successfully.",
            "email_id": email["id"],
            "to": email["to"],
            "subject": email["subject"],
            "profile_used": profile_name
        }
