from commands.base_command import BaseCommand
from context.context_manager import ContextManager


class ContextInfoCommand(BaseCommand):
    """
    Príkaz, ktorý vypíše obsah kontextu:
    - krátkodobú pamäť
    - dlhodobú pamäť
    - stav systému
    - história (počet snapshotov)
    - validácia konzistencie
    """

    name = "context-info"
    description = "Zobrazí diagnostiku kontextu AI (rozšírená verzia)."

    def __init__(self, context: ContextManager):
        self.context = context

    def execute(self, *args, **kwargs):
        output = ["KONTEKST AI — DIAGNOSTIKA\n"]

        # ============================================================
        #  VALIDÁCIA KONTEXTU
        # ============================================================
        is_valid = self.context.validate()
        output.append(f"Validita kontextu: {'OK' if is_valid else 'CHYBA'}")

        # ============================================================
        #  KRÁTKODOBÁ PAMÄŤ
        # ============================================================
        output.append("\nKrátkodobá pamäť (session):")
        if self.context.session_memory:
            for item in self.context.get_recent(10):
                output.append(f"  - {item}")
        else:
            output.append("  (prázdne)")

        # ============================================================
        #  DLHODOBÁ PAMÄŤ
        # ============================================================
        output.append("\nDlhodobá pamäť (persistent):")
        if self.context.persistent_memory:
            for key, value in self.context.persistent_memory.items():
                output.append(f"  - {key}: {value}")
        else:
            output.append("  (prázdne)")

        # ============================================================
        #  STAV SYSTÉMU
        # ============================================================
        output.append("\nStav systému:")
        if self.context.state:
            for key, value in self.context.state.items():
                output.append(f"  - {key}: {value}")
        else:
            output.append("  (prázdne)")

        # ============================================================
        #  HISTÓRIA SNAPSHOTOV
        # ============================================================
        output.append("\nHistória kontextu:")
        output.append(f"  Počet snapshotov: {len(self.context.history)}")
        output.append(f"  Max. kapacita: {self.context.max_history}")

        # ============================================================
        #  POSLEDNÝ SNAPSHOT (ak existuje)
        # ============================================================
        if self.context.history:
            last = self.context.history[-1]
            output.append("\nPosledný snapshot:")
            output.append(f"  - session: {len(last['session'])} položiek")
            output.append(f"  - persistent: {len(last['persistent'])} položiek")
            output.append(f"  - state: {len(last['state'])} položiek")
        else:
            output.append("\nPosledný snapshot: (žiadny uložený)")

        # ============================================================
        #  ZÁVER
        # ============================================================
        return "\n".join(output)
