# timeline_ui_component.py
# Wrapper component for TimelineUI to integrate with UIManager
# SIRIUS LOCAL AI – ui_components (Phase 4)

from .manager import UIComponent
from timeline.timeline_ui import TimelineUI  # tvoje existujúce timeline UI

class TimelineUIComponent(UIComponent):
    def __init__(self):
        self.timeline = TimelineUI()

    def mount(self):
        print("TimelineUI mounted")

    def unmount(self):
        print("TimelineUI unmounted")

    def render(self):
        # TimelineUI will later return pixel data or layout instructions
        output = self.timeline.render()
        return output
