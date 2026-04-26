# toolbar.py
from .manager import UIComponent

class Toolbar(UIComponent):
    def mount(self):
        print("Toolbar mounted")

    def unmount(self):
        print("Toolbar unmounted")

    def render(self):
        return "Rendering Toolbar"
