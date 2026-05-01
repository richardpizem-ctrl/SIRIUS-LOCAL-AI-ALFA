from runtime.runtime_manager import RuntimeManager
from typing import Dict, Any


class Sirius:
    """
    SIRIUS – hlavný vstupný bod celého systému
    - inicializuje RuntimeManager
    - poskytuje API pre prirodzený jazyk aj AI úlohy
    - slúži ako centrálna brána pre SIRIUS-LOCAL-AI
    """

    def __init__(self):
        # Inicializácia runtime
        self.rm = RuntimeManager()
        self.rm.initialize()

    # --------------------------------------------------------
    # PRIAME AI ÚLOHY
    # --------------------------------------------------------
    def task(self, goal: str, args: Dict[str, Any] = None) -> Dict[str, Any]:
        """
        Priame volanie autonómneho runtime agenta.
        """
        return self.rm.handle_ai_task(goal, args or {})

    # --------------------------------------------------------
    # PRIRODZENÝ JAZYK
    # --------------------------------------------------------
    def process(self, text: str) -> Dict[str, Any]:
        """
        Spracuje prirodzenú vetu cez NL Router.
        """
        return self.rm.handle_nl(text)

    # --------------------------------------------------------
    # SYSTÉMOVÝ KONTEXT
    # --------------------------------------------------------
    def context(self) -> Dict[str, Any]:
        """
        Vráti systémový kontext (aktívne okno, disky, atď.)
        """
        return self.rm.get_ai_context()

    # --------------------------------------------------------
    # RUNTIME ENGINE
    # --------------------------------------------------------
    def start(self):
        """
        Spustí runtime engine.
        """
        self.rm.start()

    def stop(self):
        """
        Zastaví runtime engine.
        """
        self.rm.stop()


# ------------------------------------------------------------
# GLOBÁLNA INŠTANCIA (voliteľné)
# ------------------------------------------------------------

sirius = Sirius()
