from .base_command import BaseCommand


class TriageTestCommand(BaseCommand):
    """
    TriageTestCommand 4.0
    Testovací príkaz pre AITE (Automatic Input Triage Engine).

    Novinky vo verzii 4.0:
    - integrácia s BaseCommand lifecycle
    - SECURITY FAMILY enforcement
    - risk-aware execution
    - capability flags (filesystem read)
    - NL Router metadata
    - štruktúrovaný výstup pre Workflow Engine 4.0
    """

    # ---------------------------------------------------------
    # METADATA (v4.0)
    # ---------------------------------------------------------
    name = "triage-test"
    description = "Otestuje AITE triage na zadanom súbore."
    category = "diagnostics"

    required_identity = "FAMILY"     # bezpečné pre všetkých
    risk_level = 0.1                 # nízke riziko
    capabilities = ["fs_read"]

    keywords = ["triage", "detect", "file type", "analyze"]
    examples = ["triage-test C:/path/file.png"]

    # ---------------------------------------------------------
    # INIT
    # ---------------------------------------------------------
    def __init__(self, runtime):
        self.runtime = runtime

    # ---------------------------------------------------------
    # EXECUTION (v4.0)
    # ---------------------------------------------------------
    def execute(self, *args, **kwargs):
        """
        Otestuje AITE triage na zadanom súbore.
        """
        if not args:
            return {
                "status": "error",
                "message": "Použi: triage-test <cesta>"
            }

        path = args[0]

        try:
            result = self.runtime.aite.process(path)
        except Exception as e:
            return {
                "status": "error",
                "message": "Chyba AITE",
                "exception": str(e)
            }

        return {
            "status": "success",
            "path": path,
            "triage": result
        }
