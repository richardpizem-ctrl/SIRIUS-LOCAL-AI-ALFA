from commands.base_command import BaseCommand
from context.context_manager import ContextManager


class ContextDumpCommand(BaseCommand):
    """
    Vypíše celý obsah kontextu naraz.
    """

    name = "context-dump"
    description = "Vypíše všetky dáta z kontextu (session, persistent, state)."

    def __init__(self, context: ContextManager):
        self.context = context

    def execute(self, *args):
        out = ["=== DUMP KONTEKSTU ===\n"]

        out.append("SESSION MEMORY:")
        for item in self.context.session_memory:
            out.append(f"  - {item}")
        if not self.context.session_memory:
            out.append("  (prázdne)")

        out.append("\nPERSISTENT MEMORY:")
        for k, v in self.context.persistent_memory.items():
            out.append(f"  - {k}: {v}")
        if not self.context.persistent_memory:
            out.append("  (prázdne)")

        out.append("\nSTATE:")
        for k, v in self.context.state.items():
            out.append(f"  - {k}: {v}")
        if not self.context.state:
            out.append("  (prázdne)")

        return "\n".join(out)
