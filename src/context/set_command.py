from commands.base_command import BaseCommand
from context.context_manager import ContextManager


class ContextSetCommand(BaseCommand):
    """
    Nastaví hodnotu v stave systému.
    Použitie:
      context-set mood happy
    """

    name = "context-set"
    description = "Nastaví hodnotu v kontexte (stav systému) s validáciou, snapshotom a diff."

    def __init__(self, context: ContextManager):
        self.context = context

    def execute(self, key: str = None, value: str = None, *args):
        # -----------------------------
        #  VALIDÁCIA VSTUPU
        # -----------------------------
        if key is None or value is None:
            return "Použitie: context-set <key> <value>"

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
        #  DIFF (ak existuje stará hodnota)
        # -----------------------------
        old_value = self.context.get_state(key)
        if old_value is not None and old_value != value:
            diff_info = f"(zmena: '{old_value}' → '{value}')"
        else:
            diff_info = ""

        # -----------------------------
        #  NASTAVENIE STAVU
        # -----------------------------
        self.context.set_state(key, value)

        # -----------------------------
        #  POTVRDENIE
        # -----------------------------
        return f"Nastavené: {key} = {value} {diff_info}".strip()
