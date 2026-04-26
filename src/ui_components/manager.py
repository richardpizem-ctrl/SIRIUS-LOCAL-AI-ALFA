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
    # RENDERING
    # ---------------------------------------------------------
    def render_active(self):
        """Render the currently active component."""
        if not self._active:
            return None

        instance = self._instances.get(self._active)
        if instance:
            return instance.render()

        return None

    # ---------------------------------------------------------
    # DEBUG / INTROSPECTION
    # ---------------------------------------------------------
    def list_components(self):
        """Return list of registered component names."""
        return list(self._registry.keys())

    def active_component(self):
        """Return name of active component."""
        return self._active
