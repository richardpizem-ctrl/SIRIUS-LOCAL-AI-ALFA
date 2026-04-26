# panel.py
from .manager import UIComponent

class Panel(UIComponent):
    def mount(self):
        print("Panel mounted")

    def unmount(self):
        print("Panel unmounted")

    def render(self):
        return "Rendering Panel"
