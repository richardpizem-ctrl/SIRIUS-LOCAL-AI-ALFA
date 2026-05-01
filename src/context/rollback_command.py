from commands.base_command import BaseCommand
from context.context_manager import ContextManager


class ContextRollbackCommand(BaseCommand):
    """
    Vráti kontext o N krokov späť pomocou snapshot histórie.
    """

    name = "context-rollback"
    description = "Vráti kontext o N krokov späť (snapshot rollback)."

    def __init__(self, context: ContextManager):
        self.context = context

    def execute(self, *args, **kwargs):
        # -----------------------------
        #  VALIDÁCIA VSTUPU
        # -----------------------------
        steps = args[0] if args else None

        if steps is None:
            return "Použitie: context-rollback <počet_krokov>"

        try:
            steps = int(steps)
        except ValueError:
            return "Chyba: počet krokov musí byť číslo."

        if steps <= 0:
            return "Chyba: počet krokov musí byť väčší ako 0."

        # -----------------------------
        #  VALIDÁCIA KONTEXTU
        # -----------------------------
        if hasattr(self.context, "validate") and not self.context.validate():
            return "Chyba: Kontext nie je v konzistentnom stave."

        # -----------------------------
        #  KONTROLA HISTÓRIE
        # -----------------------------
        history_len = len(self.context.history)

        if history_len == 0:
            return "Chyba: História je prázdna — nie je možné vykonať rollback."

        if steps > history_len:
            return f"Chyba: História obsahuje len {history_len} snapshotov."

        # -----------------------------
        #  ROLLBACK
        # -----------------------------
        success = self.context.rollback(steps)

        if not success:
            return "Chyba: rollback sa nepodaril."

        # -----------------------------
        #  LOGOVANIE DO STAVU
        # -----------------------------
        self.context.set_state("last_rollback_steps", str(steps))
        self.context.set_state("last_rollback_success", "true")

        return f"Kontext bol vrátený o {steps} krok(ov) späť."
