# pixel_layout_engine.py
# PixelLayoutEngine – minimal rendering engine for UI components
# SIRIUS LOCAL AI – ui_components (Phase 4)

class PixelLayoutEngine:
    """
    Minimal skeleton for PixelLayoutEngine.
    UIManager will call draw(output) after rendering a component.
    """

    def __init__(self):
        self._last_frame = None

    def clear(self):
        """Clear the current frame buffer."""
        self._last_frame = None
        print("PixelLayoutEngine: cleared")

    def draw(self, data):
        """
        Receive rendered output from UI components.
        Later this will convert data into pixel operations.
        """
        self._last_frame = data
        print(f"PixelLayoutEngine: drawing -> {data}")

    def get_last_frame(self):
        """Return last rendered frame (for debugging)."""
        return self._last_frame
