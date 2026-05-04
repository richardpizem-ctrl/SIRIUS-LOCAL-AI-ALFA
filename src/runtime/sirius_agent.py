from typing import Dict, Any
from runtime.runtime_manager import RuntimeManager


class Sirius:
    """
    SIRIUS 4.0
    Unified entrypoint for the entire SIRIUS LOCAL AI runtime.
    - Initializes RuntimeManager 4.0
    - Provides NL, AI task, and context interfaces
    - Controls runtime engine lifecycle
    """

    def __init__(self):
        # Create runtime manager
        self.rm = RuntimeManager()

        # Full initialization pipeline (plugins, modules, NL, workflows, AI loop)
        self.rm.initialize()

    # --------------------------------------------------------
    # DIRECT AI TASKS
    # --------------------------------------------------------
    def task(self, goal: str, args: Dict[str, Any] = None) -> Dict[str, Any]:
        """
        Execute an AI task through the RuntimeManager.
        """
        return self.rm.handle_ai_task(goal, args or {})

    # --------------------------------------------------------
    # NATURAL LANGUAGE PROCESSING
    # --------------------------------------------------------
    def process(self, text: str) -> Dict[str, Any]:
        """
        Process natural language input through NL Router 4.0.
        """
        return self.rm.handle_nl(text)

    # --------------------------------------------------------
    # SYSTEM CONTEXT
    # --------------------------------------------------------
    def context(self) -> Dict[str, Any]:
        """
        Return system context (ContextManager 4.0).
        """
        return self.rm.get_ai_context()

    # --------------------------------------------------------
    # RUNTIME ENGINE CONTROL
    # --------------------------------------------------------
    def start(self):
        """
        Start the runtime engine (RuntimeEngine 4.0).
        """
        self.rm.start()

    def stop(self):
        """
        Stop the runtime engine safely.
        """
        self.rm.stop()


# Global instance (not auto‑initialized)
sirius = None
