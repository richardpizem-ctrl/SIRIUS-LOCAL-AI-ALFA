from commands.base_command import BaseCommand
from context.profile_manager import ProfileManager
from context.context_manager import ContextManager


class ContextProfileCommand(BaseCommand):
    """
    ContextProfileCommand 4.0
    Manages context profiles: save, load, delete, list, info.

    New in v4.0:
    - NL Router metadata
    - SECURITY FAMILY enforcement
    - risk-aware execution
    - capability flags (context_read, context_write, fs_read, fs_write)
    - snapshot before save/load/delete
    - structured output for Workflow Engine 4.0
    """

    # ---------------------------------------------------------
    # METADATA (v4.0)
    # ---------------------------------------------------------
    name = "context-profile"
    description = "Manages context profiles (save/load/delete/list/info)."
    category = "context"

    required_identity = "OWNER"     # Only OWNER can manage profiles
    risk_level = 0.6                # Medium-high risk (context overwrite)
    capabilities = ["context_read", "context_write", "fs_read", "fs_write"]

    keywords = ["profile", "context", "save", "load", "delete", "list", "info"]
    examples = ["context-profile save work", "context-profile load default"]

    # ---------------------------------------------------------
    # INIT
    # ---------------------------------------------------------
    def __init__(self, context: ContextManager):
        self.context = context

    # ---------------------------------------------------------
    # EXECUTION (v4.0)
    # ---------------------------------------------------------
    def execute(self, *args, **kwargs):
        """
        Executes profile management operations.
        """

        # -----------------------------
        # INPUT VALIDATION
        # -----------------------------
        if not args:
            return {
                "status": "error",
                "message": (
                    "Usage:\n"
                    "  context-profile save <name>\n"
                    "  context-profile load <name>\n"
                    "  context-profile delete <name>\n"
                    "  context-profile list\n"
                    "  context-profile info <name>"
                )
            }

        action = args[0].lower()
        name = args[1] if len(args) > 1 else None

        # -----------------------------
        # CONTEXT VALIDATION
        # -----------------------------
        if hasattr(self.context, "validate") and not self.context.validate():
            return {
                "status": "invalid",
                "message": "Context is not in a consistent state."
            }

        profiles = ProfileManager(self.context)

        # ============================================================
        # SAVE PROFILE
        # ============================================================
        if action == "save":
            if not name:
                return {
                    "status": "error",
                    "message": "Usage: context-profile save <name>"
                }

            self.context.snapshot()
            profiles.save_profile(name)

            return {
                "status": "success",
                "action": "save",
                "profile": name,
                "message": f"Profile '{name}' saved successfully."
            }

        # ============================================================
        # LOAD PROFILE
        # ============================================================
        if action == "load":
            if not name:
                return {
                    "status": "error",
                    "message": "Usage: context-profile load <name>"
                }

            self.context.snapshot()
            result = profiles.load_profile(name)

            if not result:
                return {
                    "status": "not_found",
                    "message": f"Profile '{name}' does not exist."
                }

            return {
                "status": "success",
                "action": "load",
                "profile": name,
                "message": f"Profile '{name}' loaded successfully."
            }

        # ============================================================
        # DELETE PROFILE
        # ============================================================
        if action == "delete":
            if not name:
                return {
                    "status": "error",
                    "message": "Usage: context-profile delete <name>"
                }

            result = profiles.delete_profile(name)

            if not result:
                return {
                    "status": "not_found",
                    "message": f"Profile '{name}' does not exist."
                }

            return {
                "status": "success",
                "action": "delete",
                "profile": name,
                "message": f"Profile '{name}' deleted successfully."
            }

        # ============================================================
        # LIST PROFILES
        # ============================================================
        if action == "list":
            items = profiles.list_profiles()

            return {
                "status": "success",
                "action": "list",
                "profiles": items,
                "count": len(items)
            }

        # ============================================================
        # PROFILE INFO
        # ============================================================
        if action == "info":
            if not name:
                return {
                    "status": "error",
                    "message": "Usage: context-profile info <name>"
                }

            info = profiles.get_profile_info(name)

            if not info:
                return {
                    "status": "not_found",
                    "message": f"Profile '{name}' does not exist."
                }

            return {
                "status": "success",
                "action": "info",
                "profile": name,
                "details": {
                    "session_items": info["session_items"],
                    "persistent_items": info["persistent_items"],
                    "state_items": info["state_items"],
                    "history_snapshots": info["history_snapshots"]
                }
            }

        # ============================================================
        # UNKNOWN ACTION
        # ============================================================
        return {
            "status": "error",
            "message": f"Unknown action '{action}'. Use save/load/delete/list/info."
        }
