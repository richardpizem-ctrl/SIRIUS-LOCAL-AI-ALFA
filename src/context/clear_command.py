from commands.base_command import BaseCommand
from context.context_manager import ContextManager


class ContextClearCommand(BaseCommand):
    """
    Vymaže krátkodobú pamäť AI.
    Rozšírená verzia:
    - validácia kontextu
    - snapshot pred vymazaním
    - logovanie do state
    """

    name = "context-clear"
    description = "Vymaže krátkodobú pamäť (session memory) s validáciou a snapshotom."

    def __init__(self, context: ContextManager):
        self.context = context

    def execute(self, *args):
        # -----------------------------
        #  VALIDÁCIA KONTEXTU
        # -----------------------------
        if not self.context.validate():
            return "Chyba: Kontext nie je v konzistentnom stave."

        # -----------------------------
        #  SNAPSHOT PRED VYMAZANÍM
        # -----------------------------
        self.context.snapshot()

        # -----------------------------
        #  VYMAZANIE SESSION MEMORY
        # -----------------------------
        count = len(self.context.session_memory)
        self.context.session_memory.clear()

        # -----------------------------
        #  LOGOVANIE DO STAVU
        # -----------------------------
        self.context.set_state("last_clear_count", str(count))
        self.context.set_state("last_clear_action", "session_memory")

        # -----------------------------
        #  POTVRDENIE
        # -----------------------------
        return f"Krátkodobá pamäť bola vymazaná. Odstránených položiek: {count}"
