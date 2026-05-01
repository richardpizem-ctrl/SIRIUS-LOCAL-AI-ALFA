from runtime.runtime_manager import RuntimeManager
from typing import Dict, Any


class Sirius:
    """
    SIRIUS – hlavný vstupný bod celého systému
    """

    def __init__(self):
        self.rm = RuntimeManager()
        self.rm.initialize()

    # PRIAME AI ÚLOHY
    def task(self, goal: str, args: Dict[str, Any] = None) -> Dict[str, Any]:
        return self.rm.handle_ai_task(goal, args or {})

    # PRIRODZENÝ JAZYK
    def process(self, text: str) -> Dict[str, Any]:
        return self.rm.handle_nl(text)

    # SYSTÉMOVÝ KONTEXT
    def context(self) -> Dict[str, Any]:
        return self.rm.get_ai_context()

    # RUNTIME ENGINE
    def start(self):
        self.rm.start()

    def stop(self):
        self.rm.stop()


# Nepoužívať automaticky pri importe
sirius = None
