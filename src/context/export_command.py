from commands.base_command import BaseCommand
from context.context_manager import ContextManager
import json
import os


class ContextExportCommand(BaseCommand):
    """
    ContextExportCommand 4.0
    Exports the context or selected sections into a JSON file.

    New in v4.0:
    - NL Router metadata
    - SECURITY FAMILY enforcement
    - risk-aware execution
    - capability flags (context_read, fs_write)
    - structured output for Workflow Engine 4.0
    - audit trail via BaseCommand lifecycle
    """

    # ---------------------------------------------------------
    # METADATA (v4.0)
    # ---------------------------------------------------------
    name = "context-export"
    description = "Exports the context or selected sections into a JSON file."
    category = "context"

    required_identity = "OWNER"     # Only OWNER can export context
    risk_level = 0.4                # Medium risk (filesystem write)
    capabilities = ["context_read", "fs_write"]

    keywords = ["export", "context", "json", "save"]
    examples = [
        "context-export all backup.json",
        "context-export session session.json"
    ]

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
        Exports the selected context section into a JSON file.
        """

        # -----------------------------
        # INPUT VALIDATION
        # -----------------------------
        if len(args) < 2:
            return {
                "status": "error",
                "message": (
                    "Usage:\n"
                    "  context-export all <filename>\n"
                    "  context-export session <filename>\n"
                    "  context-export persistent <filename>\n"
                    "  context-export state <filename>\n"
                    "  context-export history <filename>"
                )
            }

        section = args[0].lower()
        filename = args[1]

        # -----------------------------
        # CONTEXT VALIDATION
        # -----------------------------
        if hasattr(self.context, "validate") and not self.context.validate():
            return {
                "status": "invalid",
                "message": "Context is not in a consistent state. Export aborted."
            }

        # -----------------------------
        # SELECT DATA TO EXPORT
        # -----------------------------
        if section == "all":
            data = {
                "session": self.context.session_memory,
                "persistent": self.context.persistent_memory,
                "state": self.context.state,
                "history": self.context.history,
            }

        elif section == "session":
            data = self.context.session_memory

        elif section == "persistent":
            data = self.context.persistent_memory

        elif section == "state":
            data = self.context.state

        elif section == "history":
            data = self.context.history

        else:
            return {
                "status": "error",
                "message": f"Unknown section '{section}'. Use: all/session/persistent/state/history."
            }

        # -----------------------------
        # ENSURE DIRECTORY EXISTS
        # -----------------------------
        folder = os.path.dirname(filename)
        if folder:
            os.makedirs(folder, exist_ok=True)

        # -----------------------------
        # WRITE JSON FILE
        # -----------------------------
        try:
            with open(filename, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
        except Exception as e:
            return {
                "status": "error",
                "message": "Failed to export context.",
                "exception": str(e)
            }

        # -----------------------------
        # SUCCESS RESPONSE
        # -----------------------------
        return {
            "status": "success",
            "section": section,
            "file": filename,
            "message": f"Context section '{section}' exported successfully."
        }
