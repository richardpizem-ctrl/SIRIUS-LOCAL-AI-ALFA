import os
import shutil

class Plugin:
    """
    File Manager plugin pre SIRIUS-LOCAL-AI.
    Umožňuje:
    - vytvárať priečinky
    - presúvať súbory
    - mazať súbory
    - vypisovať obsah priečinkov
    """

    def __init__(self, runtime_manager):
        self.rm = runtime_manager

    # --------------------------------------------------------
    # NL PRÍKAZY
    # --------------------------------------------------------
    def nl_commands(self):
        return {
            "vytvor priecinok": self.nl_create_folder,
            "presun subory": self.nl_move_files,
            "vymaz subor": self.nl_delete_file,
            "obsah priecinka": self.nl_list_directory
        }

    def nl_create_folder(self, text):
        path = text.strip()
        try:
            os.makedirs(path, exist_ok=True)
            return f"Priečinok vytvorený: {path}"
        except Exception as e:
            return f"Chyba pri vytváraní priečinka: {e}"

    def nl_move_files(self, text):
        try:
            src, dst = text.split("->")
            src = src.strip()
            dst = dst.strip()
            os.makedirs(dst, exist_ok=True)
            for file in os.listdir(src):
                shutil.move(os.path.join(src, file), dst)
            return f"Súbory presunuté z {src} do {dst}"
        except Exception as e:
            return f"Chyba pri presúvaní súborov: {e}"

    def nl_delete_file(self, text):
        path = text.strip()
        try:
            os.remove(path)
            return f"Súbor vymazaný: {path}"
        except Exception as e:
            return f"Chyba pri mazaní súboru: {e}"

    def nl_list_directory(self, text):
        path = text.strip()
        try:
            items = os.listdir(path)
            if not items:
                return "Priečinok je prázdny."
            return "\n".join(items)
        except Exception as e:
            return f"Chyba pri čítaní priečinka: {e}"

    # --------------------------------------------------------
    # AI TASKY
    # --------------------------------------------------------
    def ai_tasks(self):
        return {
            "create_folder": self.ai_create_folder,
            "move_files": self.ai_move_files,
            "delete_file": self.ai_delete_file,
            "list_directory": self.ai_list_directory
        }

    def ai_create_folder(self, params):
        path = params.get("path")
        os.makedirs(path, exist_ok=True)
        return {"status": "OK", "created": path}

    def ai_move_files(self, params):
        src = params.get("src")
        dst = params.get("dst")
        os.makedirs(dst, exist_ok=True)
        for file in os.listdir(src):
            shutil.move(os.path.join(src, file), dst)
        return {"status": "OK", "moved": True}

    def ai_delete_file(self, params):
        path = params.get("path")
        os.remove(path)
        return {"status": "OK", "deleted": path}

    def ai_list_directory(self, params):
        path = params.get("path")
        return {"items": os.listdir(path)}

    # --------------------------------------------------------
    # WORKFLOWY
    # --------------------------------------------------------
    def workflows(self):
        return [
            {
                "name": "auto_clean_downloads",
                "steps": [
                    {"action": "log", "message": "Čistenie priečinka Downloads..."},
                    {"action": "task", "task": "list_directory", "params": {"path": "Downloads"}},
                    {"action": "return", "value": "Hotovo."}
                ]
            }
        ]

    # --------------------------------------------------------
    # AI LOOP PRAVIDLÁ
    # --------------------------------------------------------
    def ai_loop_rules(self):
        return [
            {
                "name": "monitor_downloads",
                "trigger": "interval",
                "interval": 60,
                "action": "list_directory",
                "params": {"path": "Downloads"}
            }
        ]

    # --------------------------------------------------------
    # GUI PRVKY
    # --------------------------------------------------------
    def gui_elements(self):
        return [
            {
                "type": "button",
                "label": "Vytvoriť priečinok",
                "action": "create_folder"
            },
            {
                "type": "button",
                "label": "Presunúť súbory",
                "action": "move_files"
            }
        ]
