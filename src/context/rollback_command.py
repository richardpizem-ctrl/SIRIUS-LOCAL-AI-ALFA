from commands.base_command import BaseCommand
from context.context_manager import ContextManager


class ContextRollbackCommand(BaseCommand):
    """
    ContextRollbackCommand 4.0
    Rolls the context back by N snapshots using the snapshot history.

    New in v4.0:
    - NL Router metadata
    - SECURITY FAMILY enforcement
    - risk-aware execution
    - capability flags (context_write)
    - structured output for Workflow Engine 4.0
    """

    # ---------------------------------------------------------
    # METADATA (v4.0)
    # ---------------------------------------------------------
    name = "context-rollback"
    description = "Rolls the context back by N steps using snapshot history."
    category = "context"

    required_identity = "OWNER"     # Only OWNER can rollback context
    risk_level = 0.7                # High risk (context overwrite)
    capabilities = ["context_write"]

    keywords = ["rollback", "context", "history", "snapshot"]
    examples = ["context-rollback 3"]

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
        Rolls the context back by N snapshots.
        """

        # -----------------------------
        # INPUT VALIDATION
        # -----------------------------
        steps = args[0] if args else None

        if steps is None:
            return {
                "status": "error",
                "message": "Usage: context-rollback <steps>"
            }

        try:
            steps = int(steps)
        except ValueError:
            return {
                "status": "error",
                "message": "Steps must be a number."
            }

        if steps <= 0:
            return {
                "status": "error",
                "message": "Steps must be greater than 0."
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
        # HISTORY CHECK
        # -----------------------------
        history_len = len(self.context.history)

        if history_len == 0:
            return {
                "status": "error",
                "message": "History is empty — rollback cannot be performed."
            }

        if steps > history_len:
            return {
                "status": "error",
                "message": f"History contains only {history_len} snapshots."
            }

        # -----------------------------
        # PERFORM ROLLBACK
        # -----------------------------
        success = self.context.rollback(steps)

        if not success:
            return {
                "status": "error",
                "message": "Rollback failed."
            }

        # -----------------------------
        # LOG STATE
        # -----------------------------
        self.context.set_state("last_rollback_steps", str(steps))
        self.context.set_state("last_rollback_success", "true")

        # -----------------------------
        # SUCCESS RESPONSE
        # -----------------------------
        return {
            "status": "success",
            "rolled_back_steps": steps,
            "message": f"Context rolled back by {steps} step(s)."
        }
