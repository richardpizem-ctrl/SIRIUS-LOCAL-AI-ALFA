from commands.base_command import BaseCommand
from context.context_manager import ContextManager


class ContextClearCommand(BaseCommand):
    """
    ContextClearCommand 4.0
    Clears the short‑term (session) memory with validation, snapshot creation,
    and state logging.

    New in v4.0:
    - NL Router metadata
    - SECURITY FAMILY enforcement
    - risk‑aware execution
    - capability flags (context_write)
    - audit trail via BaseCommand lifecycle
    - structured output for Workflow Engine 4.0
    """

    # ---------------------------------------------------------
    # METADATA (v4.0)
    # ---------------------------------------------------------
    name = "context-clear"
    description = "Clears the short‑term session memory with validation and snapshot."
    category = "context"

    required_identity = "OWNER"     # Only OWNER can clear memory
    risk_level = 0.4                # Medium risk (memory modification)
    capabilities = ["context_write"]

    keywords = ["clear", "context", "session", "memory"]
    examples = ["context-clear"]

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
        Clears the session memory with validation, snapshot, and state logging.
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
        # SNAPSHOT BEFORE CLEARING
        # -----------------------------
        self.context.snapshot()

        # -----------------------------
        # CLEAR SESSION MEMORY
        # -----------------------------
        count = len(self.context.session_memory)
        self.context.session_memory.clear()

        # -----------------------------
        # LOG STATE
        # -----------------------------
        self.context.set_state("last_clear_count", str(count))
        self.context.set_state("last_clear_action", "session_memory")

        # -----------------------------
        # STRUCTURED OUTPUT
        # -----------------------------
        return {
            "status": "success",
            "cleared_items": count,
            "message": f"Session memory cleared. Removed items: {count}"
        }
