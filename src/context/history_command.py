from commands.base_command import BaseCommand
from context.context_manager import ContextManager


class ContextHistoryCommand(BaseCommand):
    """
    ContextHistoryCommand 4.0
    Displays the snapshot history of the context with optional limit.

    New in v4.0:
    - NL Router metadata
    - SECURITY FAMILY enforcement
    - risk-aware execution
    - capability flags (context_read)
    - structured output for Workflow Engine 4.0
    - audit trail via BaseCommand lifecycle
    """

    # ---------------------------------------------------------
    # METADATA (v4.0)
    # ---------------------------------------------------------
    name = "context-history"
    description = "Displays the snapshot history of the context."
    category = "context"

    required_identity = "OWNER"     # Only OWNER can inspect snapshot history
    risk_level = 0.2                # Low risk (read-only)
    capabilities = ["context_read"]

    keywords = ["history", "context", "snapshots", "memory"]
    examples = ["context-history", "context-history 5"]

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
        Displays snapshot history with optional limit.
        """

        # -----------------------------
        # VALIDATE CONTEXT
        # -----------------------------
        if hasattr(self.context, "validate") and not self.context.validate():
            return {
                "status": "invalid",
                "message": "Context is not in a consistent state."
            }

        # -----------------------------
        # HISTORY SIZE
        # -----------------------------
        total = len(self.context.history)

        if total == 0:
            return {
                "status": "empty",
                "message": "Snapshot history is empty."
            }

        # -----------------------------
        # LIMIT (optional)
        # -----------------------------
        limit = args[0] if args else None

        if limit is not None:
            try:
                limit = int(limit)
                if limit <= 0:
                    return {
                        "status": "error",
                        "message": "Limit must be greater than 0."
                    }
            except ValueError:
                return {
                    "status": "error",
                    "message": "Limit must be a number."
                }
        else:
            limit = total

        limit = min(limit, total)

        # -----------------------------
        # SELECT SNAPSHOTS
        # -----------------------------
        start_index = total - limit
        snapshots = self.context.history[start_index:]

        formatted = []
        for snap in snapshots:
            formatted.append({
                "session_items": len(snap.get("session", [])),
                "persistent_items": len(snap.get("persistent", {})),
                "state_items": len(snap.get("state", {}))
            })

        # -----------------------------
        # STRUCTURED OUTPUT
        # -----------------------------
        return {
            "status": "success",
            "total_snapshots": total,
            "showing_last": limit,
            "snapshots": formatted
        }
