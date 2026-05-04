import platform
import os
from .base_command import BaseCommand


class SystemInfoCommand(BaseCommand):
    """
    SystemInfoCommand 4.0
    Vráti základné informácie o systéme, platforme a prostredí.

    Novinky vo verzii 4.0:
    - metadata pre NL Router 4.0
    - SECURITY FAMILY integrácia
    - risk-aware execution
    - capability flags (WIN-CAP)
    - audit trail cez BaseCommand lifecycle
    - štruktúrovaný výstup pre Workflow Engine 4.0
    """

    # ---------------------------------------------------------
    # METADATA (v4.0)
    # ---------------------------------------------------------
    name = "system-info"
    description = "Zobrazí informácie o systéme, platforme a prostredí."
    category = "system"

    required_identity = "FAMILY"     # bezpečné pre všetkých
    risk_level = 0.0                 # žiadne riziko
    capabilities = ["system_read"]

    keywords = ["system", "info", "platform", "os", "environment"]
    examples = ["system-info", "show system info"]

    # ---------------------------------------------------------
    # EXECUTION
    # ---------------------------------------------------------
    def execute(self, *args, **kwargs):
        """
        Vráti prehľad základných systémových informácií.
        Výstup je štruktúrovaný pre Workflow Engine 4.0.
        """

        info = {
            "platform": platform.system(),
            "platform_release": platform.release(),
            "platform_version": platform.version(),
            "machine": platform.machine(),
            "processor": platform.processor(),
            "python_version": platform.python_version(),
            "working_directory": os.getcwd(),
        }

        # Pre CLI / NL Router môžeme vrátiť aj textovú verziu
        text_output = ["Systémové informácie:\n"]
        for key, value in info.items():
            text_output.append(f"- {key}: {value}")

        return {
            "status": "success",
            "info": info,
            "text": "\n".join(text_output)
        }
