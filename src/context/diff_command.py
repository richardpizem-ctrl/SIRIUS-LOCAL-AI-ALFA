from commands.base_command import BaseCommand
from context.context_manager import ContextManager


class ContextDiffCommand(BaseCommand):
    """
    ContextDiffCommand 4.0
    Compares the current context state with values stored in memory.

    New in v4.0:
    - NL Router metadata
    - SECURITY FAMILY enforcement
    - risk-aware execution
    - capability flags (context_read)
    - audit trail via BaseCommand lifecycle
    - structured output for Workflow Engine 4.0
    """

    # ---------------------------------------------------------
    # METADATA (v4.0)
    # ---------------------------------------------------------
    name = "context-diff"
    description = "Shows differences between the current state and stored memory."
    category = "context"

    required_identity = "OWNER"     # Only OWNER can inspect internal memory
    risk_level = 0.2                # Low risk (read-only)
    capabilities = ["context_read"]

    keywords = ["diff", "context", "compare", "memory", "state"]
    examples = ["context-diff", "context-diff mood"]

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
        Compares context state with memory values.
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
        # DIFF FOR SPECIFIC KEY
        # -----------------------------
        key = args[0] if args else None

        if key is not None:
            mem_value = self.context.recall(key)
            state_value = self.context.get_state(key)

            if mem_value is None and state_value is None:
                return {
                    "status": "not_found",
                    "key": key,
                    "message": f"No data exists for key '{key}'."
                }

            if mem_value == state_value:
                return {
                    "status": "equal",
                    "key": key,
                    "message": f"No difference for '{key}'. Values are identical.",
                    "value": mem_value
                }

            return {
                "status": "diff",
                "key": key,
                "memory": mem_value,
                "state": state_value,
                "message": f"Difference found for '{key}'."
            }

        # -----------------------------
        # DIFF FOR ENTIRE STATE
        # -----------------------------
        diff = self.context.diff(self.context.state)

        if not diff:
            return {
                "status": "equal",
                "message": "State and memory are fully consistent."
            }

        formatted = {}
        for k, info in diff.items():
            formatted[k] = {
                "current": info["current"],
                "memory": info["incoming"]
            }

        return {
            "status": "diff",
            "message": "Differences found between state and memory.",
            "diff": formatted
        }
