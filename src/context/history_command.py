from commands.base_command import BaseCommand
from context.context_manager import ContextManager


class ContextHistoryCommand(BaseCommand):
    """
    Zobrazí históriu snapshotov kontextu.
    Použitie:
      context-history
      context-history 5   -> zobrazí posledných 5 snapshotov
    """

    name = "context-history"
    description = "Zobrazí históriu snapshotov kontextu."

    def __init__(self, context: ContextManager):
        self.context = context

    def execute(self, *args, **kwargs):
        # -----------------------------
        #  VALIDÁCIA KONTEXTU
        # -----------------------------
        if hasattr(self.context, "validate") and not self.context.validate():
            return "Chyba: Kontext nie je v konzistentnom stave."

        # -----------------------------
        #  LIMIT (voliteľný)
        # -----------------------------
        max_items = len(self.context.history)
        limit = args[0] if args else None

        if limit is not None:
            try:
                limit = int(limit)
                if limit <= 0:
                    return "Chyba: limit musí byť väčší ako 0."
            except ValueError:
                return "Chyba: limit musí byť číslo."
        else:
            limit = max_items

        # Normalizácia limitu
        limit = min(limit, max_items)

        # -----------------------------
        #  KONTROLA HISTÓRIE
        # -----------------------------
        if max_items == 0:
            return "História je prázdna — žiadne snapshoty."

        # -----------------------------
        #  PRÍPRAVA VÝSTUPU
        # -----------------------------
        out = ["=== HISTÓRIA SNAPSHOTOV ===\n"]
        out.append(f"Celkový počet snapshotov: {max_items}")
        out.append(f"Zobrazujem posledných: {limit}\n")

        # -----------------------------
        #  VÝPIS SNAPSHOTOV
        # -----------------------------
        start_index = max_items - limit
        snapshots = self.context.history[start_index:]

        for i, snap in enumerate(snapshots, start=1):
            out.append(f"Snapshot #{i}:")
            out.append(f"  - session: {len(snap['session'])} položiek")
            out.append(f"  - persistent: {len(snap['persistent'])} položiek")
            out.append(f"  - state: {len(snap['state'])} položiek")
            out.append("")

        return "\n".join(out)
