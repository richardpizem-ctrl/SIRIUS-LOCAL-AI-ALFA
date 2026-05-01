import pyperclip

class Plugin:
    """
    Clipboard plugin pre SIRIUS-LOCAL-AI.
    Umožňuje čítať a zapisovať text do systémovej schránky.
    """

    def __init__(self, runtime_manager):
        self.rm = runtime_manager

    # --------------------------------------------------------
    # NL PRÍKAZY
    # --------------------------------------------------------
    def nl_commands(self):
        return {
            "skopiruj": self.nl_copy,
            "vloz": self.nl_paste,
            "schranka": self.nl_read_clipboard
        }

    def nl_copy(self, text):
        pyperclip.copy(text)
        return f"Skopírované do schránky: {text}"

    def nl_paste(self, text):
        content = pyperclip.paste()
        return f"Zo schránky: {content}"

    def nl_read_clipboard(self, text):
        content = pyperclip.paste()
        return f"Schránka obsahuje: {content}"

    # --------------------------------------------------------
    # AI TASKY
    # --------------------------------------------------------
    def ai_tasks(self):
        return {
            "clipboard_copy": self.ai_copy,
            "clipboard_paste": self.ai_paste,
            "clipboard_read": self.ai_read
        }

    def ai_copy(self, params):
        text = params.get("text", "")
        pyperclip.copy(text)
        return {"status": "OK", "copied": text}

    def ai_paste(self, params):
        content = pyperclip.paste()
        return {"status": "OK", "content": content}

    def ai_read(self, params):
        content = pyperclip.paste()
        return {"clipboard": content}

    # --------------------------------------------------------
    # WORKFLOWY
    # --------------------------------------------------------
    def workflows(self):
        return [
            {
                "name": "clipboard_log",
                "steps": [
                    {"action": "log", "message": "Čítam obsah schránky..."},
                    {"action": "task", "task": "clipboard_read"},
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
                "name": "clipboard_monitor",
                "trigger": "interval",
                "interval": 90,
                "action": "clipboard_read",
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
                "label": "Kopírovať text",
                "action": "clipboard_copy",
                "params": {"text": "Ahoj svet"}
            },
            {
                "type": "button",
                "label": "Vložiť zo schránky",
                "action": "clipboard_paste"
            },
            {
                "type": "button",
                "label": "Zobraziť schránku",
                "action": "clipboard_read"
            }
        ]
