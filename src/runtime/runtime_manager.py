from .engine import RuntimeEngine
from .event_bus import EventBus
from triage.aite_controller import AITEController
from filesystem.fs_agent import FSAgent
from .win_capabilities import WorkflowEngine


class RuntimeManager:
    """
    Runtime Manager
    - centrálna orchestrácia runtime systému
    - drží RuntimeEngine, EventBus, FS‑AGENT, AITE a WorkflowEngine
    - poskytuje jednotné API pre vyššie vrstvy (NL router, AI agent)
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

        # AITE (AI Triage Engine)
        self.aite = AITEController()

        # Prepojenie AITE → FS‑AGENT
        self.aite.attach_fs_agent(self.fs_agent)

        # Prepojenie AITE → WorkflowEngine (ak bude potrebné)
        if hasattr(self.aite, "attach_workflow"):
            self.aite.attach_workflow(self.workflow)

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
