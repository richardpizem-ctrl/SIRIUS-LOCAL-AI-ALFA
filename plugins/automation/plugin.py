import subprocess
import sys
import os

class Plugin:
    """
    Automation plugin pre SIRIUS-LOCAL-AI.
    Umožňuje spúšťať shell príkazy, skripty a automatizované úlohy.
    """

    def __init__(self, runtime_manager):
        self.rm = runtime_manager

    # --------------------------------------------------------
    # NL PRÍKAZY
    # --------------------------------------------------------
    def nl_commands(self):
        return {
            "spusti prikaz": self.nl_run_command,
            "spusti skript": self.nl_run_script
        }

    def nl_run_command(self, text):
        try:
            result = subprocess.check_output(text, shell=True, stderr=subprocess.STDOUT, encoding="utf-8")
            return f"Výstup:\n{result}"
        except subprocess.CalledProcessError as e:
            return f"Chyba:\n{e.output}"

    def nl_run_script(self, text):
        script = text.strip()
        if not os.path.exists(script):
            return "Skript neexistuje."
        try:
            result = subprocess.check_output([sys.executable, script], stderr=subprocess.STDOUT, encoding="utf-8")
            return f"Výstup skriptu:\n{result}"
        except subprocess.CalledProcessError as e:
            return f"Chyba skriptu:\n{e.output}"

    # --------------------------------------------------------
    # AI TASKY
    # --------------------------------------------------------
    def ai_tasks(self):
        return {
            "run_command": self.ai_run_command,
            "run_script": self.ai_run_script
        }

    def ai_run_command(self, params):
        cmd = params.get("cmd")
        if not cmd:
            return {"error": "Missing 'cmd' parameter."}
        try:
            result = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT, encoding="utf-8")
            return {"status": "OK", "output": result}
        except subprocess.CalledProcessError as e:
            return {"error": e.output}

    def ai_run_script(self, params):
        script = params.get("script")
        if not script or not os.path.exists(script):
            return {"error": "Script not found."}
        try:
            result = subprocess.check_output([sys.executable, script], stderr=subprocess.STDOUT, encoding="utf-8")
            return {"status": "OK", "output": result}
        except subprocess.CalledProcessError as e:
            return {"error": e.output}

    # --------------------------------------------------------
    # WORKFLOWY
    # --------------------------------------------------------
    def workflows(self):
        return [
            {
                "name": "auto_cleanup",
                "steps": [
                    {"action": "log", "message": "Spúšťam automatické čistenie..."},
                    {"action": "task", "task": "run_command", "params": {"cmd": "echo Cistenie hotove"}},
                    {"action": "return", "value": "Automatizácia dokončená."}
                ]
            }
        ]

    # --------------------------------------------------------
    # AI LOOP PRAVIDLÁ
    # --------------------------------------------------------
    def ai_loop_rules(self):
        return [
            {
                "name": "automation_heartbeat",
                "trigger": "interval",
                "interval": 240,
                "action": "run_command",
                "params": {"cmd": "echo Heartbeat OK"}
            }
        ]

    # --------------------------------------------------------
    # GUI PRVKY
    # --------------------------------------------------------
    def gui_elements(self):
        return [
            {
                "type": "button",
                "label": "Spusti test príkaz",
                "action": "run_command",
                "params": {"cmd": "echo Test OK"}
            },
            {
                "type": "button",
                "label": "Spusti skript",
                "action": "run_script",
                "params": {"script": "test.py"}
            }
        ]
