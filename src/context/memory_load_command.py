from commands.base_command import BaseCommand
from context.context_manager import ContextManager


class MemoryLoadCommand(BaseCommand):
    """
    Načíta hodnotu z dlhodobej pamäte.
    Použitie:
      memory-load <key>
    """

    name = "memory-load"
    description = "Načíta hodnotu z dlhodobej pamäte AI (s validáciou, diff a bezpečným merge)."

    def __init__(self, context: ContextManager):
        self.context = context

    def execute(self, *args, **kwargs):
        # -----------------------------
        #  VALIDÁCIA VSTUPU
        # -----------------------------
        key = args[0] if args else None
        if key is None:
            return "Použitie: memory-load <key>"

        # -----------------------------
        #  VALIDÁCIA KONTEXTU
        # -----------------------------
        if hasattr(self.context, "validate") and not self.context.validate():
            return "Chyba: Kontext nie je v konzistentnom stave."

        # -----------------------------
        #  NAČÍTANIE HODNOTY
        # -----------------------------
        value = self.context.recall(key)
        if value is None:
            return f"V pamäti sa nenašlo: {key}"

        # -----------------------------
        #  DIFF
        # -----------------------------
        state_value = self.context.get_state(key)
        if state_value is not None and state_value != value:
            diff_info = f"(stav sa líši: state='{state_value}' vs memory='{value}')"
        else:
            diff_info = ""

        # -----------------------------
        #  SNAPSHOT PRED ZMENOU
        # -----------------------------
        if hasattr(self.context, "snapshot"):
            self.context.snapshot()

        # -----------------------------
        #  BEZPEČNÝ MERGE
        # -----------------------------
        if isinstance(key, str):
            self.context.merge({key: value})

        # -----------------------------
        #  POTVRDENIE
        # -----------------------------
        return f"{key} = {value} {diff_info}".strip()
