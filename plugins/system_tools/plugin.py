import platform
import psutil
import shutil

class Plugin:
    """
    System Tools plugin pre SIRIUS-LOCAL-AI.
    Poskytuje informácie o systéme, CPU, RAM, disku a OS.
    """

    def __init__(self, runtime_manager):
        self.rm = runtime_manager

    # --------------------------------------------------------
    # NL PRÍKAZY
    # --------------------------------------------------------
    def nl_commands(self):
        return {
            "system info": self.nl_system_info,
            "cpu info": self.nl_cpu_info,
            "ram info": self.nl_ram_info,
            "disk info": self.nl_disk_info
        }

    def nl_system_info(self, text):
        return self._system_info()

    def nl_cpu_info(self, text):
        return f"CPU: {psutil.cpu_percent()}%"

    def nl_ram_info(self, text):
        ram = psutil.virtual_memory()
        return f"RAM: {ram.percent}%"

    def nl_disk_info(self, text):
        disk = shutil.disk_usage("/")
        percent = (disk.used / disk.total) * 100
        return f"Disk: {percent:.2f}%"

    # --------------------------------------------------------
    # AI TASKY
    # --------------------------------------------------------
    def ai_tasks(self):
        return {
            "system_info": self.ai_system_info,
            "cpu_usage": self.ai_cpu_usage,
            "ram_usage": self.ai_ram_usage,
            "disk_usage": self.ai_disk_usage
        }

    def ai_system_info(self, params):
        return self._system_info_dict()

    def ai_cpu_usage(self, params):
        return {"cpu_percent": psutil.cpu_percent()}

    def ai_ram_usage(self, params):
        ram = psutil.virtual_memory()
        return {"ram_percent": ram.percent}

    def ai_disk_usage(self, params):
        disk = shutil.disk_usage("/")
        percent = (disk.used / disk.total) * 100
        return {"disk_percent": percent}

    # --------------------------------------------------------
    # WORKFLOWY
    # --------------------------------------------------------
    def workflows(self):
        return [
            {
                "name": "system_diagnostics",
                "steps": [
                    {"action": "log", "message": "Spúšťam diagnostiku systému..."},
                    {"action": "task", "task": "system_info"},
                    {"action": "return", "value": "Diagnostika dokončená."}
                ]
            }
        ]

    # --------------------------------------------------------
    # AI LOOP PRAVIDLÁ
    # --------------------------------------------------------
    def ai_loop_rules(self):
        return [
            {
                "name": "system_heartbeat",
                "trigger": "interval",
                "interval": 180,
                "action": "system_info",
                "params": {}
            }
        ]

    # --------------------------------------------------------
    # GUI PRVKY
    # --------------------------------------------------------
    def gui_elements(self):
        return [
            {
                "type": "button",
                "label": "System Info",
                "action": "system_info"
            },
            {
                "type": "button",
                "label": "CPU",
                "action": "cpu_usage"
            },
            {
                "type": "button",
                "label": "RAM",
                "action": "ram_usage"
            },
            {
                "type": "button",
                "label": "Disk",
                "action": "disk_usage"
            }
        ]

    # --------------------------------------------------------
    # INTERNÉ FUNKCIE
    # --------------------------------------------------------
    def _system_info(self):
        info = self._system_info_dict()
        return (
            f"OS: {info['os']}\n"
            f"CPU: {info['cpu']}\n"
            f"RAM: {info['ram_percent']}%\n"
            f"Disk: {info['disk_percent']:.2f}%"
        )

    def _system_info_dict(self):
        ram = psutil.virtual_memory()
        disk = shutil.disk_usage("/")
        return {
            "os": platform.platform(),
            "cpu": f"{psutil.cpu_percent()}%",
            "ram_percent": ram.percent,
            "disk_percent": (disk.used / disk.total) * 100
        }

