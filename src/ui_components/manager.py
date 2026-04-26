# manager.py
# UI Manager – central registry and lifecycle controller for UI components
# SIRIUS LOCAL AI – ui_components (Phase 4)

from typing import Dict, Type, Optional


class UIComponent:
    """
    Base class for all UI components.
    Every component must implement:
        - mount()
        - unmount()
        - render()
    """
    def mount(self):
        raise NotImplementedError

    def unmount(self):
        raise NotImplementedError

    def render(self):
        raise NotImplementedError


class UIManager:
    """
    Central orchestrator for all UI components.
    Handles:
        - component registration
        - component lifecycle
        - active component switching
        - safe mounting/unmounting
        - integration with PixelLayoutEngine (later)
    """

    def __init__(self):
        self._registry: Dict[str, Type[UIComponent]] = {}
        self._instances: Dict[str, UIComponent] = {}
        self._active: Optional[str] = None
        self._layout_engine = None  # added for PixelLayoutEngine integration

    # ---------------------------------------------------------
    # REGISTRATION
    # ---------------------------------------------------------
    def register(self, name: str, component_cls: Type[UIComponent]):
        """Register a UI component class under a unique name."""
        if name in self._registry:
            raise ValueError(f"UI component '{name}' already registered")

        self._registry[name] = component_cls

    def unregister(self, name: str):
        """Remove a component from registry."""
        if name in self._instances:
            self._instances[name].unmount()
            del self._instances[name]

        self._registry.pop(name, None)

    # ---------------------------------------------------------
    # COMPONENT ACCESS
    # ---------------------------------------------------------
    def get(self, name: str) -> UIComponent:
        """Return an instance of a component, creating it if needed."""
        if name not in self._registry:
            raise KeyError(f"UI component '{name}' not found")

        if name not in self._instances:
            self._instances[name] = self._registry[name]()

        return self._instances[name]

    # ---------------------------------------------------------
    # LIFECYCLE CONTROL
    # ---------------------------------------------------------
    def activate(self, name: str):
        """Activate a component and deactivate the previous one."""
        if name not in self._registry:
            raise KeyError(f"UI component '{name}' not found")

        # Unmount previous
        if self._active and self._active in self._instances:
            self._instances[self._active].unmount()

        # Mount new
        instance = self.get(name)
        instance.mount()

        self._active = name

    def deactivate(self):
        """Deactivate the currently active component."""
        if self._active and self._active in self._instances:
            self._instances[self._active].unmount()

        self._active = None

    # ---------------------------------------------------------
    # LAYOUT ENGINE INTEGRATION
    # ---------------------------------------------------------
    def connect_layout_engine(self, engine):
        """Attach PixelLayoutEngine instance."""
        self._layout_engine = engine

    # ---------------------------------------------------------
    # RENDERING
    # ---------------------------------------------------------
    def render_active(self):
        """Render the currently active component."""
        if not self._active:
            return None

        instance = self._instances.get(self._active)
        if not instance:
            return None

        output = instance.render()

        # Forward to PixelLayoutEngine if connected
        if self._layout_engine:
            self._layout_engine.draw(output)

        return output

    # ---------------------------------------------------------
    # DEBUG / INTROSPECTION
    # ---------------------------------------------------------
    def list_components(self):
        """Return list of registered component names."""
        return list(self._registry.keys())

    def active_component(self):
        """Return name of active component."""
        return self._active


# ---------------------------------------------------------
# TEMPORARY TEST BLOCK
# ---------------------------------------------------------
if __name__ == "__main__":
    from panel import Panel
    from window import Window
    from toolbar import Toolbar
    from timeline_ui_component import TimelineUIComponent
    from pixel_layout_engine import PixelLayoutEngine

    ui = UIManager()
    ui.register("panel", Panel)
    ui.register("window", Window)
    ui.register("toolbar", Toolbar)
    ui.register("timeline", TimelineUIComponent)

    # Connect PixelLayoutEngine
    engine = PixelLayoutEngine()
    ui.connect_layout_engine(engine)

    ui.activate("panel")
    print(ui.render_active())

    ui.activate("window")
    print(ui.render_active())

    ui.activate("toolbar")
    print(ui.render_active())

    ui.activate("timeline")
    print(ui.render_active())
