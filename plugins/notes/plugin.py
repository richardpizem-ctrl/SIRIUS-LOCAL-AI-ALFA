import os
import datetime

class Plugin:
    """
    Notes plugin pre SIRIUS-LOCAL-AI.
    Umožňuje zapisovať, čítať, listovať a mazať poznámky.
    """

    def __init__(self, runtime_manager):
        self.rm = runtime_manager
        self.storage = "notes_storage"
        os.makedirs(self.storage, exist_ok=True)

    # --------------------------------------------------------
    # NL PRÍKAZY
    # --------------------------------------------------------
    def nl_commands(self):
        return {
            "zapíš poznámku": self.nl_write_note,
            "zobraz poznámky": self.nl_list_notes,
            "čítaj poznámku": self.nl_read_note,
            "vymaž poznámku": self.nl_delete_note
        }

    def nl_write_note(self, text):
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{self.storage}/note_{timestamp}.txt"
        with open(filename, "w", encoding="utf-8") as f:
            f.write(text)
        return f"Poznámka uložená: {filename}"

    def nl_list_notes(self, text):
        files = os.listdir(self.storage)
        if not files:
            return "Žiadne poznámky."
        return "\n".join(files)

    def nl_read_note(self, text):
        filename = f"{self.storage}/{text.strip()}"
        if not os.path.exists(filename):
            return "Poznámka neexistuje."
        with open(filename, "r", encoding="utf-8") as f:
            return f.read()

    def nl_delete_note(self, text):
        filename = f"{self.storage}/{text.strip()}"
        if not os.path.exists(filename):
            return "Poznámka neexistuje."
        os.remove(filename)
        return f"Poznámka vymazaná: {filename}"

    # --------------------------------------------------------
    # AI TASKY
    # --------------------------------------------------------
    def ai_tasks(self):
        return {
            "write_note": self.ai_write_note,
            "read_note": self.ai_read_note,
            "list_notes": self.ai_list_notes,
            "delete_note": self.ai_delete_note
        }

    def ai_write_note(self, params):
        text = params.get("text", "")
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{self.storage}/note_{timestamp}.txt"
        with open(filename, "w", encoding="utf-8") as f:
            f.write(text)
        return {"status": "OK", "file": filename}

    def ai_read_note(self, params):
        name = params.get("name")
        filename = f"{self.storage}/{name}"
        if not os.path.exists(filename):
            return {"error": "Note not found"}
        with open(filename, "r", encoding="utf-8") as f:
            return {"content": f.read()}

    def ai_list_notes(self, params):
        return {"notes": os.listdir(self.storage)}

    def ai_delete_note(self, params):
        name = params.get("name")
        filename = f"{self.storage}/{name}"
        if not os.path.exists(filename):
            return {"error": "Note not found"}
        os.remove(filename)
        return {"status": "OK", "deleted": name}

    # --------------------------------------------------------
    # WORKFLOWY
    # --------------------------------------------------------
    def workflows(self):
        return [
            {
                "name": "daily_note",
                "steps": [
                    {"action": "log", "message": "Zapisujem dennú poznámku..."},
                    {"action": "task", "task": "write_note", "params": {"text": "Denný záznam."}},
                    {"action": "return", "value": "Denná poznámka uložená."}
                ]
            }
        ]

    # --------------------------------------------------------
    # AI LOOP PRAVIDLÁ
    # --------------------------------------------------------
    def ai_loop_rules(self):
        return [
            {
                "name": "notes_heartbeat",
                "trigger": "interval",
                "interval": 300,
                "action": "list_notes",
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
                "label": "Zobraziť poznámky",
                "action": "list_notes"
            },
            {
                "type": "button",
                "label": "Zapísať rýchlu poznámku",
                "action": "write_note",
                "params": {"text": "Rýchla poznámka."}
            }
        ]
