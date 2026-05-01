from commands.base_command import BaseCommand
from context.context_manager import ContextManager
import json
import os
import copy


class RestoreCommand(BaseCommand):
    """
    Obnoví kontext zo súboru vytvoreného príkazom context-backup.
    """

    name = "context-restore"
    description = "Obnoví celý kontext zo záložného JSON súboru."

    def __init__(self, context: ContextManager, backup_dir="backups"):
        self.context = context
        self.backup_dir = backup_dir

    def execute(self, *args, **kwargs):
        # -----------------------------
        #  VALIDÁCIA VSTUPU
        # -----------------------------
        filename = args[0] if args else None

        if filename is None:
            return (
                "Použitie:\n"
                "  context-restore <filename>\n\n"
                "Príklad:\n"
                "  context-restore backup_2026-04-24_11-25-55.json"
            )

        filepath = filename

        # Ak používateľ zadal len názov, doplníme cestu backups/
        if not os.path.isfile(filepath):
            candidate = os.path.join(self.backup_dir, filename)
            if os.path.isfile(candidate):
                filepath = candidate
            else:
                return f"Chyba: súbor '{filename}' neexistuje ani v '{self.backup_dir}/'."

        # -----------------------------
        #  NAČÍTANIE JSON
        # -----------------------------
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                data = json.load(f)
        except Exception as e:
            return f"Chyba pri načítaní backup súboru: {e}"

        # -----------------------------
        #  VALIDÁCIA OBSAHU BACKUPU
        # -----------------------------
        required_keys = ["session", "persistent", "state", "history"]

        if not isinstance(data, dict) or not all(k in data for k in required_keys):
            return "Chyba: backup súbor nemá správnu štruktúru (session/persistent/state/history)."

        # typová validácia
        if not isinstance(data["session"], list):
            return "Chyba: session musí byť zoznam."
        if not isinstance(data["persistent"], dict):
            return "Chyba: persistent musí byť objekt."
        if not isinstance(data["state"], dict):
            return "Chyba: state musí byť objekt."
        if not isinstance(data["history"], list):
            return "Chyba: history musí byť zoznam snapshotov."

        # -----------------------------
        #  OBNOVA KONTEXTU (deep copy)
        # -----------------------------
        self.context.session_memory = copy.deepcopy(data["session"])
        self.context.persistent_memory = copy.deepcopy(data["persistent"])
        self.context.state = copy.deepcopy(data["state"])

        # rešpektovať max_history
        self.context.history = copy.deepcopy(
            data["history"][-self.context.max_history:]
        )

        # -----------------------------
        #  SNAPSHOT PO OBNOVE
        # -----------------------------
        if hasattr(self.context, "snapshot"):
            self.context.snapshot()

        # -----------------------------
        #  VALIDÁCIA PO OBNOVE
        # -----------------------------
        if hasattr(self.context, "validate") and not self.context.validate():
            return (
                "Upozornenie: Kontext bol obnovený, "
                "ale nie je v konzistentnom stave."
            )

        return f"Kontext bol obnovený zo súboru '{filepath}'."
