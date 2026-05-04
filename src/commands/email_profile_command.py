from commands.base_command import BaseCommand
from email.manager import EmailManager


class EmailProfileCommand(BaseCommand):
    """
    EmailProfileCommand 4.0
    Manages email sender profiles (create, list, delete, show).

    New in v4.0:
    - NL Router metadata
    - SECURITY FAMILY enforcement
    - OWNER-only execution
    - structured JSON output
    - safe profile management pipeline
    """

    # ---------------------------------------------------------
    # METADATA (v4.0)
    # ---------------------------------------------------------
    name = "email-profile"
    description = "Manages email sender profiles."
    category = "email"

    required_identity = "OWNER"     # Only OWNER can manage profiles
    risk_level = 0.4                # Medium risk (writes to storage)
    capabilities = ["fs_read", "fs_write"]

    keywords = ["email", "profile", "sender", "identity"]
    examples = [
        "email-profile list",
        "email-profile create myprofile John john@example.com",
        "email-profile delete myprofile",
        "email-profile show myprofile"
    ]

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
        Profile management:
            email-profile list
            email-profile show <name>
            email-profile delete <name>
            email-profile create <name> <display_name> <email>
        """

        # -----------------------------
        # INPUT VALIDATION
        # -----------------------------
        if len(args) < 1:
            return {
                "status": "error",
                "message": "Usage: email-profile <list|show|delete|create> ..."
            }

        action = args[0].lower()

        # ============================================================
        # LIST PROFILES
        # ============================================================
        if action == "list":
            profiles = self.email_manager.list_profiles()
            return {
                "status": "success",
                "action": "list",
                "count": len(profiles),
                "profiles": profiles
            }

        # ============================================================
        # SHOW PROFILE
        # ============================================================
        if action == "show":
            if len(args) < 2:
                return {
                    "status": "error",
                    "message": "Usage: email-profile show <name>"
                }

            name = args[1]
            profile = self.email_manager.load_profile(name)

            if profile is None:
                return {
                    "status": "error",
                    "message": f"Profile '{name}' not found."
                }

            return {
                "status": "success",
                "action": "show",
                "profile_name": name,
                "profile": profile
            }

        # ============================================================
        # DELETE PROFILE
        # ============================================================
        if action == "delete":
            if len(args) < 2:
                return {
                    "status": "error",
                    "message": "Usage: email-profile delete <name>"
                }

            name = args[1]

            if hasattr(self.context, "snapshot"):
                self.context.snapshot()

            success = self.email_manager.delete_profile(name)

            if not success:
                return {
                    "status": "error",
                    "message": f"Profile '{name}' not found."
                }

            self.context.merge({"last_email_profile_deleted": name})

            return {
                "status": "success",
                "action": "delete",
                "profile_name": name,
                "message": f"Profile '{name}' deleted."
            }

        # ============================================================
        # CREATE PROFILE
        # ============================================================
        if action == "create":
            if len(args) < 4:
                return {
                    "status": "error",
                    "message": "Usage: email-profile create <name> <display_name> <email>"
                }

            name = args[1]
            display_name = args[2]
            email = args[3]

            if hasattr(self.context, "snapshot"):
                self.context.snapshot()

            profile = {
                "name": display_name,
                "email": email
            }

            self.email_manager.save_profile(name, profile)

            self.context.merge({
                "last_email_profile_created": name
            })

            return {
                "status": "success",
                "action": "create",
                "profile_name": name,
                "profile": profile,
                "message": f"Profile '{name}' created."
            }

        # ============================================================
        # UNKNOWN ACTION
        # ============================================================
        return {
            "status": "error",
            "message": "Unknown action. Use: list | show | delete | create"
        }
