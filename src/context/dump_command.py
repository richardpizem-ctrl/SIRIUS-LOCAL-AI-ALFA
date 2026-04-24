from commands.base_command import BaseCommand
from context.context_manager import ContextManager


class ContextDumpCommand(BaseCommand):
    """
    Vypíše celý obsah kontextu naraz.
    Rozšírená verzia obsahuje:
    - validáciu kontextu
    - snapshot históriu
    - diagnostiku posledného snapshotu
    - počty položiek v jednotlivých sekciách
    """

    name = "context-dump"
    description = "Vypíše všetky dáta z kontextu (session, persistent, state, história)."

    def __init__(self, context: ContextManager):
        self.context = context

    def execute(self, *args):
        out = ["=== DUMP KONTEKSTU ===\n"]

        # ============================================================
        #  VALIDITA KONTEXTU
        # ============================================================
        is_valid = self.context.validate()
        out.append(f"Validita kontextu: {'OK' if is_valid else 'CHYBA'}\n")

        # ============================================================
        #  SESSION MEMORY
        # ============================================================
        out.append("SESSION MEMORY:")
        if self.context.session_memory:
            out.append(f"  (počet: {len(self.context.session_memory)})")
            for item in self.context.session_memory:
                out.append(f"  - {item}")
        else:
            out.append("  (prázdne)")

        # ============================================================
        #  PERSISTENT MEMORY
        # ============================================================
        out.append("\nPERSISTENT MEMORY:")
        if self.context.persistent_memory:
            out.append(f"  (počet: {len(self.context.persistent_memory)})")
            for k, v in self.context.persistent_memory.items():
                out.append(f"  - {k}: {v}")
        else:
            out.append("  (prázdne)")

        # ============================================================
        #  STATE
        # ============================================================
        out.append("\nSTATE:")
        if self.context.state:
            out.append(f"  (počet: {len(self.context.state)})")
            for k, v in self.context.state.items():
                out.append(f"  - {k}: {v}")
        else:
            out.append("  (prázdne)")

        # ============================================================
        #  HISTÓRIA SNAPSHOTOV
        # ============================================================
        out.append("\nHISTÓRIA SNAPSHOTOV:")
        out.append(f"  Počet snapshotov: {len(self.context.history)}")
        out.append(f"  Max. kapacita: {self.context.max_history}")

        # ============================================================
        #  POSLEDNÝ SNAPSHOT (DETAILY)
        # ============================================================
        if self.context.history:
            last = self.context.history[-1]
            out.append("\nPosledný snapshot:")
            out.append(f"  - session: {len(last['session'])} položiek")
            out.append(f"  - persistent: {len(last['persistent'])} položiek")
            out.append(f"  - state: {len(last['state'])} položiek")
        else:
            out.append("\nPosledný snapshot: (žiadny uložený)")

        # ============================================================
        #  ZÁVER
        # ============================================================
        return "\n".join(out)
