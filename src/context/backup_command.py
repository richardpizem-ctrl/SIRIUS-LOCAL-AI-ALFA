from commands.base_command import BaseCommand
from context.context_manager import ContextManager
import json
import os
from datetime import datetime


class ContextBackupCommand(BaseCommand):
    """
    ContextBackupCommand 4.0
    Vytvorí timestampovaný backup celého kontextu do priečinka backups/.

    Novinky vo verzii 4.0:
    - metadata pre NL Router 4.0
    - SECURITY FAMILY enforcement
    - risk-aware execution
    - capability flags (filesystem write)
    - audit trail cez BaseCommand lifecycle
    - štruktúrovaný výstup pre Workflow Engine 4.0
    """

    # ---------------------------------------------------------
    # METADATA (v4.0)
    # ---------------------------------------------------------
    name = "context-backup"
    description = "Vytvorí timestampovaný backup celého kontextu do priečinka backups/."
    category = "context"

    required_identity = "OWNER"     # iba OWNER môže robiť backup
    risk_level = 0.3                # mierne riziko (práca so súbormi)
    capabilities = ["fs_write"]

    keywords = ["backup", "context", "save", "export"]
    examples = ["context-backup", "context-backup my_backup.json"]

    # ---------------------------------------------------------
    # INIT
    # ---------------------------------------------------------
    def __init__(self, context: ContextManager, backup_dir="backups"):
        self.context = context
        self.backup_dir = backup_dir

    # ---------------------------------------------------------
    # EXECUTION (v4.0)
    # ---------------------------------------------------------
    def execute(self, *args, **kwargs):
        """
        Vytvorí timestampovaný backup kontextu.
        """
        # -----------------------------
        # VALIDÁCIA KONTEXTU
        # -----------------------------
        if hasattr(self.context, "validate"):
            if not self.context.validate():
                return {
                    "status": "invalid",
                    "message": "Kontext nie je v konzistentnom stave. Backup zrušený."
                }

        # -----------------------------
        # GENEROVANIE NÁZVU SÚBORU
        # -----------------------------
        filename = args[0] if args else None

        if filename is None:
            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            filename = f"backup_{timestamp}.json"

        # -----------------------------
        # PRIEČINOK
        # -----------------------------
        os.makedirs(self.backup_dir, exist_ok=True)
        filepath = os.path.join(self.backup_dir, filename)

        # -----------------------------
        # PRÍPRAVA DÁT NA BACKUP
        # -----------------------------
        data = {
            "timestamp": datetime.now().isoformat(),
            "session": self.context.session_memory,
            "persistent": self.context.persistent_memory,
            "state": self.context.state,
            "history": self.context.history,
        }

        # -----------------------------
        # ZÁPIS DO SÚBORU
        # -----------------------------
        try:
            with open(filepath, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
        except Exception as e:
            return {
                "status": "error",
                "message": "Chyba pri vytváraní backupu.",
                "exception": str(e)
            }

        return {
            "status": "success",
            "file": filepath,
            "message": "Backup bol úspešne vytvorený."
        }
