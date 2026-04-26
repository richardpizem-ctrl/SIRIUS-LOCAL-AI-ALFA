# window.py
from .manager import UIComponent

class Window(UIComponent):
    def mount(self):
        print("Window mounted")

    def unmount(self):
        print("Window unmounted")

    def render(self):
        return "Rendering Window"
