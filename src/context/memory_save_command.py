from commands.base_command import BaseCommand
from context.context_manager import ContextManager


class MemorySaveCommand(BaseCommand):
    """
    MemorySaveCommand 4.0
    Saves a key-value pair into persistent memory with validation,
    snapshot creation, diff reporting, and safe merge into state.

    New in v4.0:
    - NL Router metadata
    - SECURITY FAMILY enforcement
    - risk-aware execution
    - capability flags (context_write)
    - snapshot before modification
    - diff reporting
    - structured output for Workflow Engine 4.0
    """

    # ---------------------------------------------------------
    # METADATA (v4.0)
    # ---------------------------------------------------------
    name = "memory-save"
    description = "Saves a value into persistent memory and merges it into state."
    category = "context"

    required_identity = "OWNER"     # Only OWNER can modify persistent memory
    risk_level = 0.5                # Medium risk (persistent + state modification)
    capabilities = ["context_write"]

    keywords = ["memory", "save", "persistent", "store"]
    examples = ["memory-save language english"]

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
        Saves a persistent memory value and merges it into state.
        """

        # -----------------------------
        # INPUT VALIDATION
        # -----------------------------
        if len(args) < 2:
            return {
                "status": "error",
                "message": "Usage: memory-save <key> <value>"
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
        old_value = self.context.recall(key)
        diff = None

        if old_value is not None and old_value != value:
            diff = {
                "old": old_value,
                "new": value
            }

        # -----------------------------
        # SAVE TO PERSISTENT MEMORY
        # -----------------------------
        self.context.store(key, value)

        # -----------------------------
        # SAFE MERGE INTO STATE
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
            "message": f"Value '{key}' saved to persistent memory."
        }
