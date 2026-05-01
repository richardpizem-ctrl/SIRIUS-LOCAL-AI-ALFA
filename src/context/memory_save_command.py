from commands.base_command import BaseCommand
from context.context_manager import ContextManager


class MemorySaveCommand(BaseCommand):
    """
    Uloží hodnotu do dlhodobej pamäte.
    Použitie:
      memory-save <key> <value>
    """

    name = "memory-save"
    description = "Uloží hodnotu do dlhodobej pamäte AI (s validáciou, snapshotom a diff)."

    def __init__(self, context: ContextManager):
        self.context = context

    def execute(self, *args, **kwargs):
        # -----------------------------
        #  VALIDÁCIA VSTUPU
        # -----------------------------
        if len(args) < 2:
            return "Použitie: memory-save <key> <value>"

        key, value = args[0], args[1]

        # -----------------------------
        #  VALIDÁCIA KONTEXTU
        # -----------------------------
        if hasattr(self.context, "validate") and not self.context.validate():
            return "Chyba: Kontext nie je v konzistentnom stave."

        # -----------------------------
        #  SNAPSHOT PRED ZMENOU
        # -----------------------------
        if hasattr(self.context, "snapshot"):
            self.context.snapshot()

        # -----------------------------
        #  DIFF
        # -----------------------------
        old_value = self.context.recall(key)
        if old_value is not None and old_value != value:
            diff_info = f"(zmena: '{old_value}' → '{value}')"
        else:
            diff_info = ""

        # -----------------------------
        #  ULOŽENIE DO PAMÄTE
        # -----------------------------
        self.context.store(key, value)

        # -----------------------------
        #  MERGE DO STAVU (voliteľné, ale odporúčané)
        # -----------------------------
        if isinstance(key, str):
            self.context.merge({key: value})

        # -----------------------------
        #  POTVRDENIE
        # -----------------------------
        return f"Uložené do pamäte: {key} = {value} {diff_info}".strip()
