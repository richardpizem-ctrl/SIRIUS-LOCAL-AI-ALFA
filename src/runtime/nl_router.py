def register(self, phrase: str, fn):
    """
    Registruje NL príkaz z pluginu.
    Podporuje pattern matching.
    """
    self.dynamic_commands[phrase.lower()] = fn


def handle(self, text: str) -> Dict[str, Any]:
    text = text.lower().strip()

    # ----------------------------------------------------
    # 1) Pluginové NL príkazy (pattern match)
    # ----------------------------------------------------
    for phrase, fn in self.dynamic_commands.items():
        if phrase in text:
            try:
                result = fn(text, self.rm)
                return {"plugin": result}
            except Exception as e:
                return {"error": str(e)}

    # ----------------------------------------------------
    # 2) Tvoje pôvodné rule-based príkazy
    # ----------------------------------------------------
    # (tvoj pôvodný kód ostáva)

    # ----------------------------------------------------
    # 3) Fallback: AITE
    # ----------------------------------------------------
    aite_result = self.rm.aite.process(text)
    if aite_result is not None:
        return {"aite": aite_result}

    # ----------------------------------------------------
    # 4) Fallback: SiriusAgent interpret
    # ----------------------------------------------------
    agent_result = self.agent.run_task("interpret", {"text": text})
    if agent_result is not None:
        return {"agent": agent_result}

    return {"ok": False, "error": "Nerozumiem príkazu."}
