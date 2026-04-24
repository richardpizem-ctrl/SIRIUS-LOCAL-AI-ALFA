from commands.base_command import BaseCommand
from context.context_manager import ContextManager


class MemorySaveCommand(BaseCommand):
    """
    Uloží hodnotu do dlhodobej pamäte.
    Použitie:
      memory-save language english
    """

    name = "memory-save"
    description = "Uloží hodnotu do dlhodobej pamäte AI (s validáciou, snapshotom a diff)."

    def __init__(self, context: ContextManager):
        self.context = context

    def execute(self, key: str = None, value: str = None, *args):
        # -----------------------------
        #  VALIDÁCIA VSTUPU
        # -----------------------------
        if key is None or value is None:
            return "Použitie: memory-save <key> <value>"

        # -----------------------------
        #  VALIDÁCIA KONTEXTU
        # -----------------------------
        if not self.context.validate():
            return "Chyba: Kontext nie je v konzistentnom stave."

        # -----------------------------
        #  SNAPSHOT PRED ZMENOU
        # -----------------------------
        self.context.snapshot()

        # -----------------------------
        #  DIFF (ak už existuje stará hodnota)
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
        #  POTVRDENIE
        # -----------------------------
        return f"Uložené do pamäte: {key} = {value} {diff_info}".strip()
