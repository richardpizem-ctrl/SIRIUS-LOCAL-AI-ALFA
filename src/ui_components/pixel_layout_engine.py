# pixel_layout_engine.py
# PixelLayoutEngine – central renderer for UI layout blocks
# SIRIUS LOCAL AI – ui_components (Phase 4)

from typing import List, Dict, Any

class PixelLayoutEngine:
    """
    PixelLayoutEngine prijíma layout bloky od UI komponentov
    a vykresľuje ich do cieľového výstupu (terminál, canvas, GUI, atď.)

    V tejto fáze (Phase 4) ide o stabilný skeleton:
        - render_blocks() prijíma list blokov
        - validate_block() kontroluje správnosť formátu
        - render() vykonáva samotné vykreslenie (placeholder)
        - clear() resetuje buffer
        - get_last_frame() vracia posledný render
    """

    def __init__(self):
        self._last_frame = None

    # ---------------------------------------------------------
    # Buffer management
    # ---------------------------------------------------------

    def clear(self):
        """Clear the current frame buffer."""
        self._last_frame = None
        print("PixelLayoutEngine: cleared")

    def get_last_frame(self):
        """Return last rendered frame (for debugging)."""
        return self._last_frame

    # ---------------------------------------------------------
    # Validation
    # ---------------------------------------------------------

    def validate_block(self, block: Dict[str, Any]) -> bool:
        """
        Overí, či blok obsahuje minimálne:
            - type
            - x, y
        """
        required = ["type", "x", "y"]
        return all(key in block for key in required)

    # ---------------------------------------------------------
    # Rendering pipeline
    # ---------------------------------------------------------

    def render_blocks(self, blocks: List[Dict[str, Any]]):
        """
        Hlavná metóda – prijíma layout bloky z UI komponentu.
        V Phase 4 vykonáva len bezpečné logovanie a kontrolu.
        """
        if not isinstance(blocks, list):
            raise ValueError("render_blocks() očakáva list blokov")

        validated = []
        for block in blocks:
            if self.validate_block(block):
                validated.append(block)
            else:
                print(f"[PixelLayoutEngine] Ignorujem nevalidný blok: {block}")

        self._last_frame = validated
        self.render(validated)

    def render(self, blocks: List[Dict[str, Any]]):
        """
        Placeholder renderer.
        V budúcnosti sa tu napojí:
            - terminálový renderer
            - GUI renderer
            - canvas renderer
            - animácie
        """
        print("\n[PixelLayoutEngine] Rendering layout:")
        for block in blocks:
            print(f"  → {block}")
