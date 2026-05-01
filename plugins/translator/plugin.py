class Plugin:
    """
    Translator plugin pre SIRIUS-LOCAL-AI.
    Umožňuje prekladať texty pomocou ContextManager.translate().
    """

    def __init__(self, runtime_manager):
        self.rm = runtime_manager
        self.ctx = runtime_manager.context

    # --------------------------------------------------------
    # NL PRÍKAZY
    # --------------------------------------------------------
    def nl_commands(self):
        return {
            "preloz do": self.nl_translate,
            "translate to": self.nl_translate
        }

    def nl_translate(self, text):
        """
        Formát:
        preloz do en Ahoj svet
        translate to de Hello world
        """
        parts = text.split(" ", 1)
        if len(parts) < 2:
            return "Použitie: preloz do <lang> <text>"

        lang = parts[0].strip()
        sentence = parts[1].strip()

        try:
            result = self.ctx.translate(sentence, lang)
            return f"Preklad ({lang}): {result}"
        except Exception as e:
            return f"Chyba pri preklade: {e}"

    # --------------------------------------------------------
    # AI TASKY
    # --------------------------------------------------------
    def ai_tasks(self):
        return {
            "translate_text": self.ai_translate_text
        }

    def ai_translate_text(self, params):
        text = params.get("text")
        lang = params.get("lang")

        if not text or not lang:
            return {"error": "Missing 'text' or 'lang' parameter."}

        result = self.ctx.translate(text, lang)
        return {
            "status": "OK",
            "translated": result,
            "target_lang": lang
        }

    # --------------------------------------------------------
    # WORKFLOWY
    # --------------------------------------------------------
    def workflows(self):
        return [
            {
                "name": "auto_translate_log",
                "steps": [
                    {"action": "log", "message": "Automatický preklad textu..."},
                    {"action": "task", "task": "translate_text", "params": {"text": "Hello world", "lang": "sk"}},
                    {"action": "return", "value": "Workflow prekladu dokončený."}
                ]
            }
        ]

    # --------------------------------------------------------
    # AI LOOP PRAVIDLÁ
    # --------------------------------------------------------
    def ai_loop_rules(self):
        return [
            {
                "name": "translator_heartbeat",
                "trigger": "interval",
                "interval": 120,
                "action": "translate_text",
                "params": {"text": "System check", "lang": "sk"}
            }
        ]

    # --------------------------------------------------------
    # GUI PRVKY
    # --------------------------------------------------------
    def gui_elements(self):
        return [
            {
                "type": "button",
                "label": "Prelož do EN",
                "action": "translate_text",
                "params": {"lang": "en", "text": "Ahoj svet"}
            },
            {
                "type": "button",
                "label": "Prelož do DE",
                "action": "translate_text",
                "params": {"lang": "de", "text": "Ahoj svet"}
            }
        ]
