from .engine import RuntimeEngine
from .event_bus import EventBus
from triage.aite_controller import AITEController
from filesystem.fs_agent import FSAgent


class RuntimeManager:
    def __init__(self):
        self.engine = RuntimeEngine()
        self.events = EventBus()

        # FS‑AGENT
        self.fs_agent = FSAgent()

        # AITE
        self.aite = AITEController()
        self.aite.attach_fs_agent(self.fs_agent)   # ← prepojenie AITE → FS‑AGENT

    def initialize(self):
        # TODO: register modules here
        pass

    def start(self):
        self.engine.start()

    def stop(self):
        self.engine.stop()
