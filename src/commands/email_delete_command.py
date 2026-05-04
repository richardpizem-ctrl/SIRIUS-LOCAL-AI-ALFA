from commands.base_command import BaseCommand
from email.manager import EmailManager


class EmailDeleteCommand(BaseCommand):
    """
    EmailDeleteCommand 4.0
    Deletes an email (draft or sent) by ID using EmailManager.
    """

    name = "email-delete"
    description = "Deletes an email draft or sent email by ID."
    category = "email"

    required_identity = "OWNER"
    risk_level = 0.5
    capabilities = ["fs_write"]

    keywords = ["email", "delete", "remove"]
    examples = ["email-delete 20260424_112233"]

    def __init__(self, context, email_manager: EmailManager):
        self.context = context
        self.email_manager = email_manager

    def execute(self, *args, **kwargs):
        if len(args) < 1:
            return {
                "status": "error",
                "message": "Usage: email-delete <email_id>"
            }

        email_id = args[0]

        if hasattr(self.context, "snapshot"):
            self.context.snapshot()

        success = self.email_manager.delete_email(email_id)

        if not success:
            return {
                "status": "error",
                "message": f"Email '{email_id}' not found."
            }

        self.context.merge({
            "last_email_deleted_id": email_id
        })

        return {
            "status": "success",
            "message": f"Email '{email_id}' deleted successfully.",
            "email_id": email_id
        }
