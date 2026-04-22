from commands.base_command import BaseCommand
from context.context_manager import ContextManager


class ContextInfoCommand(BaseCommand):
    """
    Príkaz, ktorý vypíše obsah kontextu:
    - krátkodobú pamäť
    - dlhodobú pamäť
    - stav systému
    """

    name = "context-info"
    description = "Zobrazí diagnostiku kontextu AI."

    def __init__(self, context: ContextManager):
        self.context = context

    def execute(self, *args, **kwargs):
        output = ["KONTEKST AI — DIAGNOSTIKA\n"]

        # Krátkodobá pamäť
        output.append("Krátkodobá pamäť (session):")
        if self.context.session_memory:
            for item in self.context.get_recent(10):
                output.append(f"  - {item}")
        else:
            output.append("  (prázdne)")

        # Dlhodobá pamäť
        output.append("\nDlhodobá pamäť (persistent):")
        if self.context.persistent_memory:
            for key, value in self.context.persistent_memory.items():
                output.append(f"  - {key}: {value}")
        else:
            output.append("  (prázdne)")

        # Stav systému
        output.append("\nStav systému:")
        if self.context.state:
            for key, value in self.context.state.items():
                output.append(f"  - {key}: {value}")
        else:
            output.append("  (prázdne)")

        return "\n".join(output)
