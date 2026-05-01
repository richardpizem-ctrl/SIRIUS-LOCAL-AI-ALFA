from .engine import RuntimeEngine
from .event_bus import EventBus
from triage.aite_controller import AITEController
from filesystem.fs_agent import FSAgent
from .win_capabilities import WorkflowEngine
from .sirius_agent import SiriusAgent
from typing import Dict, Any, Optional


class RuntimeManager:
    """
    Runtime Manager
    - centrálna orchestrácia runtime systému
    - drží RuntimeEngine, EventBus, FS‑AGENT, AITE, WorkflowEngine a SiriusAgent
    - poskytuje jednotné API pre vyššie vrstvy (NL router, AI agent, SIRIUS-LOCAL-AI)
    """

    def __init__(self):
        # CORE ENGINE
        self.engine = RuntimeEngine()

        # EVENT BUS
        self.events = EventBus()

        # FS‑AGENT (nízkoúrovňové operácie so súbormi)
        self.fs_agent = FSAgent()

        # WORKFLOW ENGINE (vysoká logika)
        self.workflow = WorkflowEngine()

        # AUTONÓMNY AI AGENT (SiriusAgent)
        self.agent = SiriusAgent(self.workflow)

        # AITE (AI Triage Engine)
        self.aite = AITEController()

        # Prepojenie AITE → FS‑AGENT
        self.aite.attach_fs_agent(self.fs_agent)

        # Prepojenie AITE → WorkflowEngine (ak existuje podpora)
        if hasattr(self.aite, "attach_workflow"):
            self.aite.attach_workflow(self.workflow)

        # Prepojenie AITE → SiriusAgent (ak existuje podpora)
        if hasattr(self.aite, "attach_agent"):
            self.aite.attach_agent(self.agent)

    def initialize(self):
        """
        Miesto pre registráciu modulov, listenerov, hookov.
        """
        pass

    def start(self):
        """
        Spustí runtime engine.
        """
        self.engine.start()

    def stop(self):
        """
        Zastaví runtime engine.
        """
        self.engine.stop()

    # --------------------------------------------------------
    # SIRIUS-LOCAL-AI API VRSTVA
    # --------------------------------------------------------

    def handle_ai_task(self, goal: str, args: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Vstupný bod pre SIRIUS-LOCAL-AI:
        - goal: názov úlohy (napr. 'prepare_release', 'move_logs', 'open_project', 'snap_right')
        - args: parametre úlohy
        """
        return self.agent.run_task(goal, args or {})

    def get_ai_context(self) -> Dict[str, Any]:
        """
        Poskytne AI základný systémový kontext (napr. aktívne okno, disky).
        """
        return self.workflow.cme.execute("system_state", {})
