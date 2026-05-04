from commands.base_command import BaseCommand
from context.context_manager import ContextManager
import json
import os
import copy


class ContextMergeCommand(BaseCommand):
    """
    ContextMergeCommand 4.0
    Merges an external JSON context file into the current context.

    New in v4.0:
    - NL Router metadata
    - SECURITY FAMILY enforcement
    - high‑risk classification
    - capability flags (context_write, fs_read)
    - snapshot before merge
    - deep‑copy safety
    - structured output for Workflow Engine 4.0
    """

    # ---------------------------------------------------------
    # METADATA (v4.0)
    # ---------------------------------------------------------
    name = "context-merge"
    description = "Merges an external JSON context file into the current context."
    category = "context"

    required_identity = "OWNER"     # Only OWNER can merge external context
    risk_level = 0.8                # High risk (massive context modification)
    capabilities = ["context_write", "fs_read"]

    keywords = ["merge", "context", "import", "combine"]
    examples = ["context-merge all backup.json"]

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
        Merges external JSON context into the current context.
        """

        # -----------------------------
        # INPUT VALIDATION
        # -----------------------------
        if len(args) < 2:
            return {
                "status": "error",
                "message": (
                    "Usage:\n"
                    "  context-merge all <filename>\n"
                    "  context-merge session <filename>\n"
                    "  context-merge persistent <filename>\n"
                    "  context-merge state <filename>\n"
                    "  context-merge history <filename>"
                )
            }

        section = args[0].lower()
        filename = args[1]

        if not os.path.isfile(filename):
            return {
                "status": "error",
                "message": f"File '{filename}' does not exist."
            }

        # -----------------------------
        # LOAD JSON
        # -----------------------------
        try:
            with open(filename, "r", encoding="utf-8") as f:
                incoming = json.load(f)
        except Exception as e:
            return {
                "status": "error",
                "message": "Failed to load JSON file.",
                "exception": str(e)
            }

        # -----------------------------
        # SNAPSHOT BEFORE MERGE
        # -----------------------------
        if hasattr(self.context, "snapshot"):
            self.context.snapshot()

        # -----------------------------
        # MERGE BY SECTION
        # -----------------------------
        try:
            if section == "all":
                if not isinstance(incoming, dict):
                    return {
                        "status": "error",
                        "message": "JSON must contain an object."
                    }

                # SESSION
                if isinstance(incoming.get("session"), list):
                    for item in incoming["session"]:
                        if isinstance(item, str):
                            self.context.session_memory.append(item)

                # PERSISTENT
                if isinstance(incoming.get("persistent"), dict):
                    for k, v in incoming["persistent"].items():
                        if isinstance(k, str) and isinstance(v, str):
                            self.context.persistent_memory[k] = v

                # STATE
                if isinstance(incoming.get("state"), dict):
                    for k, v in incoming["state"].items():
                        if isinstance(k, str) and isinstance(v, str):
                            self.context.state[k] = v

                # HISTORY
                if isinstance(incoming.get("history"), list):
                    for snap in incoming["history"]:
                        if isinstance(snap, dict):
                            self.context.history.append(copy.deepcopy(snap))

                    # enforce max_history
                    self.context.history = self.context.history[-self.context.max_history:]

            elif section == "session":
                if not isinstance(incoming, list):
                    return {"status": "error", "message": "Session must be a list."}
                for item in incoming:
                    if isinstance(item, str):
                        self.context.session_memory.append(item)

            elif section == "persistent":
                if not isinstance(incoming, dict):
                    return {"status": "error", "message": "Persistent must be an object."}
                for k, v in incoming.items():
                    if isinstance(k, str) and isinstance(v, str):
                        self.context.persistent_memory[k] = v

            elif section == "state":
                if not isinstance(incoming, dict):
                    return {"status": "error", "message": "State must be an object."}
                for k, v in incoming.items():
                    if isinstance(k, str) and isinstance(v, str):
                        self.context.state[k] = v

            elif section == "history":
                if not isinstance(incoming, list):
                    return {"status": "error", "message": "History must be a list of snapshots."}
                for snap in incoming:
                    if isinstance(snap, dict):
                        self.context.history.append(copy.deepcopy(snap))
                self.context.history = self.context.history[-self.context.max_history:]

            else:
                return {
                    "status": "error",
                    "message": f"Unknown section '{section}'."
                }

        except Exception as e:
            return {
                "status": "error",
                "message": "Merge failed due to an internal error.",
                "exception": str(e)
            }

        # -----------------------------
        # VALIDATE AFTER MERGE
        # -----------------------------
        if hasattr(self.context, "validate") and not self.context.validate():
            return {
                "status": "warning",
                "message": "Merge completed, but context is not in a consistent state."
            }

        # -----------------------------
        # SUCCESS RESPONSE
        # -----------------------------
        return {
            "status": "success",
            "section": section,
            "file": filename,
            "message": f"Context section '{section}' merged successfully."
        }
