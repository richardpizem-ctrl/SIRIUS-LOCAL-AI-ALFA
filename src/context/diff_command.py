from commands.base_command import BaseCommand
from context.context_manager import ContextManager


class ContextDiffCommand(BaseCommand):
    """
    Porovná aktuálny stav kontextu s hodnotami v pamäti.
    Použitie:
      context-diff                -> diff celého state
      context-diff mood           -> diff pre konkrétny key
    """

    name = "context-diff"
    description = "Zobrazí rozdiely medzi stavom systému a pamäťou."

    def __init__(self, context: ContextManager):
        self.context = context

    def execute(self, *args, **kwargs):
        # -----------------------------
        #  VALIDÁCIA KONTEXTU
        # -----------------------------
        if hasattr(self.context, "validate") and not self.context.validate():
            return "Chyba: Kontext nie je v konzistentnom stave."

        # -----------------------------
        #  DIFF PRE KONKRÉTNY KEY
        # -----------------------------
        key = args[0] if args else None

        if key is not None:
            mem_value = self.context.recall(key)
            state_value = self.context.get_state(key)

            if mem_value is None and state_value is None:
                return f"Pre kľúč '{key}' neexistujú žiadne dáta."

            if mem_value == state_value:
                return f"Žiadny rozdiel pre '{key}'. Hodnota je rovnaká."

            return (
                f"Rozdiel pre '{key}':\n"
                f"  - memory: {mem_value}\n"
                f"  - state:  {state_value}"
            )

        # -----------------------------
        #  DIFF PRE CELÝ STATE
        # -----------------------------
        diff = self.context.diff(self.context.state)

        if not diff:
            return "Žiadne rozdiely — state a pamäť sú konzistentné."

        out = ["=== DIFF KONTEKSTU ===\n"]

        for k, info in diff.items():
            out.append(f"{k}:")
            out.append(f"  - current:  {info['current']}")
            out.append(f"  - memory:   {info['incoming']}\n")

        return "\n".join(out)
