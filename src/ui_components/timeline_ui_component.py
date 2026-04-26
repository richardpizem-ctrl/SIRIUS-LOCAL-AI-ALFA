# timeline_ui_component.py
# Wrapper component for TimelineUI to integrate with UIManager
# SIRIUS LOCAL AI – ui_components (Phase 4)

from .manager import UIComponent
from timeline.timeline_ui import TimelineUI  # tvoje existujúce TimelineUI

class TimelineUIComponent(UIComponent):
    """
    UI wrapper pre TimelineUI.
    Poskytuje:
        - mount / unmount lifecycle
        - render() → vracia layout bloky
        - generate_layout() → pripravuje pixelové bloky pre PixelLayoutEngine
    """

    def __init__(self):
        self.timeline = TimelineUI()
        self._mounted = False

    def mount(self):
        self._mounted = True
        print("TimelineUI mounted")

    def unmount(self):
        self._mounted = False
        print("TimelineUI unmounted")

    def generate_layout(self):
        """
        TimelineUI v budúcnosti vráti skutočné pixelové bloky.
        Zatiaľ placeholder, aby PixelLayoutEngine mal konzistentný vstup.
        """
        if hasattr(self.timeline, "generate_layout"):
            return self.timeline.generate_layout()

        # Fallback placeholder – bezpečný pre Phase 4
        return [
            {
                "type": "text",
                "x": 10,
                "y": 10,
                "content": "TimelineUI – layout placeholder",
            }
        ]

    def render(self):
        """
        UIManager volá render() → ten musí vrátiť layout bloky.
        PixelLayoutEngine ich následne vykreslí.
        """
        layout = self.generate_layout()
        return layout
