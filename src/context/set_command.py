from commands.base_command import BaseCommand
from context.context_manager import ContextManager


class ContextSetCommand(BaseCommand):
    """
    ContextSetCommand 4.0
    Sets a value in the system state with validation, snapshot,
    diff reporting, and safe merge.

    New in v4.0:
    - NL Router metadata
    - SECURITY FAMILY enforcement
    - risk-aware execution
    - capability flags (context_write)
    - snapshot before modification
    - structured output for Workflow Engine 4.0
    """

    # ---------------------------------------------------------
    # METADATA (v4.0)
    # ---------------------------------------------------------
    name = "context-set"
    description = "Sets a value in the context state with validation, snapshot, and diff."
    category = "context"

    required_identity = "OWNER"     # Only OWNER can modify system state
    risk_level = 0.4                # Medium risk (state modification)
    capabilities = ["context_write"]

    keywords = ["set", "context", "state", "update"]
    examples = ["context-set mood happy"]

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
        Sets a state variable with snapshot and diff reporting.
        """

        # -----------------------------
        # INPUT VALIDATION
        # -----------------------------
        if len(args) < 2:
            return {
                "status": "error",
                "message": "Usage: context-set <key> <value>"
            }

        key, value = args[0], args[1]

        # -----------------------------
        # CONTEXT VALIDATION
        # -----------------------------
        if hasattr(self.context, "validate") and not self.context.validate():
            return {
                "status": "invalid",
                "message": "Context is not in a consistent state."
            }

        # -----------------------------
        # SNAPSHOT BEFORE CHANGE
        # -----------------------------
        if hasattr(self.context, "snapshot"):
            self.context.snapshot()

        # -----------------------------
        # DIFF (old vs new)
        # -----------------------------
        old_value = self.context.get_state(key)
        diff = None

        if old_value is not None and old_value != value:
            diff = {
                "old": old_value,
                "new": value
            }

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
            "message": f"State variable '{key}' updated."
        }
