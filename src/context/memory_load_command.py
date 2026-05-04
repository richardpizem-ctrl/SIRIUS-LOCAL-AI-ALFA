from commands.base_command import BaseCommand
from context.context_manager import ContextManager


class MemoryLoadCommand(BaseCommand):
    """
    MemoryLoadCommand 4.0
    Loads a value from persistent memory and safely merges it into state.

    New in v4.0:
    - NL Router metadata
    - SECURITY FAMILY enforcement
    - risk-aware execution
    - capability flags (context_read, context_write)
    - diff reporting
    - snapshot before merge
    - structured output for Workflow Engine 4.0
    """

    # ---------------------------------------------------------
    # METADATA (v4.0)
    # ---------------------------------------------------------
    name = "memory-load"
    description = "Loads a value from persistent memory and merges it into state."
    category = "context"

    required_identity = "OWNER"     # Only OWNER can load memory into state
    risk_level = 0.4                # Medium risk (state modification)
    capabilities = ["context_read", "context_write"]

    keywords = ["memory", "load", "persistent", "state"]
    examples = ["memory-load language"]

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
        Loads a persistent memory value and merges it into state.
        """

        # -----------------------------
        # INPUT VALIDATION
        # -----------------------------
        key = args[0] if args else None
        if key is None:
            return {
                "status": "error",
                "message": "Usage: memory-load <key>"
            }

        # -----------------------------
        # CONTEXT VALIDATION
        # -----------------------------
        if hasattr(self.context, "validate") and not self.context.validate():
            return {
                "status": "invalid",
                "message": "Context is not in a consistent state."
            }

        # -----------------------------
        # LOAD VALUE FROM MEMORY
        # -----------------------------
        value = self.context.recall(key)
        if value is None:
            return {
                "status": "not_found",
                "key": key,
                "message": f"No value found in persistent memory for '{key}'."
            }

        # -----------------------------
        # DIFF CHECK
        # -----------------------------
        state_value = self.context.get_state(key)
        diff = None

        if state_value != value:
            diff = {
                "state": state_value,
                "memory": value
            }

        # -----------------------------
        # SNAPSHOT BEFORE MERGE
        # -----------------------------
        if hasattr(self.context, "snapshot"):
            self.context.snapshot()

        # -----------------------------
        # SAFE MERGE
        # -----------------------------
        if isinstance(key, str):
            self.context.merge({key: value})

        # -----------------------------
        # SUCCESS RESPONSE
        # -----------------------------
        return {
            "status": "success",
            "key": key,
            "value": value,
            "diff": diff,
            "message": f"Loaded '{key}' from persistent memory."
        }
