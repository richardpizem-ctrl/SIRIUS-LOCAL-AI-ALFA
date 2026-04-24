from commands.base_command import BaseCommand
from context.context_manager import ContextManager
import json
import os
from datetime import datetime


class ContextBackupCommand(BaseCommand):
    """
    Vytvorí timestampovaný backup celého kontextu.
    Použitie:
      context-backup
      context-backup <custom_filename>
    """

    name = "context-backup"
    description = "Vytvorí timestampovaný backup celého kontextu do priečinka backups/."

    def __init__(self, context: ContextManager, backup_dir="backups"):
        self.context = context
        self.backup_dir = backup_dir

        # Vytvor priečinok ak neexistuje
        if not os.path.exists(self.backup_dir):
            os.makedirs(self.backup_dir)

    def execute(self, filename: str = None, *args):
        # -----------------------------
        #  VALIDÁCIA KONTEXTU
        # -----------------------------
        if not self.context.validate():
            return "Chyba: Kontext nie je v konzistentnom stave. Backup zrušený."

        # -----------------------------
        #  GENEROVANIE NÁZVU SÚBORU
        # -----------------------------
        if filename is None:
            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            filename = f"backup_{timestamp}.json"

        filepath = os.path.join(self.backup_dir, filename)

        # -----------------------------
        #  PRÍPRAVA DÁT NA BACKUP
        # -----------------------------
        data = {
            "session": self.context.session_memory,
            "persistent": self.context.persistent_memory,
            "state": self.context.state,
            "history": self.context.history,
        }

        # -----------------------------
        #  ZÁPIS DO SÚBORU
        # -----------------------------
        try:
            with open(filepath, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
        except Exception as e:
            return f"Chyba pri vytváraní backupu: {e}"

        # -----------------------------
        #  POTVRDENIE
        # -----------------------------
        return f"Backup bol vytvorený: {filepath}"
