from .engine import RuntimeEngine
from .event_bus import EventBus

class RuntimeManager:
    def __init__(self):
        self.engine = RuntimeEngine()
        self.events = EventBus()

    def initialize(self):
        # TODO: register modules here
        pass

    def start(self):
        self.engine.start()

    def stop(self):
        self.engine.stop()
