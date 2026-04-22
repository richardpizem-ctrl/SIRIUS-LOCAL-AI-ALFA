import platform
import os
from .base_command import BaseCommand


class SystemInfoCommand(BaseCommand):
    """
    Príkaz, ktorý vráti základné informácie o systéme.
    """

    name = "system-info"
    description = "Zobrazí informácie o systéme, platforme a prostredí."

    def execute(self, *args, **kwargs):
        """
        Vráti prehľad základných systémových informácií.
        """
        info = {
            "platform": platform.system(),
            "platform-release": platform.release(),
            "platform-version": platform.version(),
            "machine": platform.machine(),
            "processor": platform.processor(),
            "python-version": platform.python_version(),
            "working-directory": os.getcwd(),
        }

        output_lines = ["Systémové informácie:\n"]
        for key, value in info.items():
            output_lines.append(f"- {key}: {value}")

        return "\n".join(output_lines)

