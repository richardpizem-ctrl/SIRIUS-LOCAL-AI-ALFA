# timeline_ui.py
# Core Timeline UI logic – generates layout blocks for PixelLayoutEngine
# SIRIUS LOCAL AI – timeline (Phase 4)

from typing import List, Dict, Any


class TimelineUI:
    """
    TimelineUI je logická vrstva časovej osi.
    Nevie nič o konkrétnom rendereri – generuje len layout bloky.

    V Phase 4 poskytuje:
        - základný grid (C4 adaptive)
        - header
        - placeholder pre eventy
        - snapping overlay (C1)
        - ghost dragging overlay (C2)
        - selection overlay (C3)
        - marker types (C5)
    """

    def __init__(self):
        self.width = 120
        self.height = 20
        self.grid_step = 10
        self.zoom = 1.0  # C4 – placeholder zoom level

        # Placeholder eventy
        self._events = [
            {
                "x": 5,
                "y": 4,
                "width": 15,
                "height": 3,
                "label": "Demo event",
            }
        ]

        # Placeholder vybraný event (C3)
        self._selected_event = {
            "x": 5,
            "y": 4,
            "width": 15,
            "height": 3,
        }

        # ---------------------------------------------------------
        # C5 – Marker types (Unicode + text)
        # ---------------------------------------------------------
        self._markers = [
            {
                "x": 10,
                "y": 2,
                "icon": "🔵",
                "label": "Section Start",
                "color": "blue",
            },
            {
                "x": 40,
                "y": 2,
                "icon": "🟢",
                "label": "Loop Start",
                "color": "green",
            },
            {
                "x": 80,
                "y": 2,
                "icon": "🔴",
                "label": "Error",
                "color": "red",
            }
        ]

    # ---------------------------------------------------------
    # Public API
    # ---------------------------------------------------------

    def render(self) -> List[Dict[str, Any]]:
        layout: List[Dict[str, Any]] = []

        layout.extend(self._build_header())
        layout.extend(self._build_grid())              # C4 adaptive grid
        layout.extend(self._build_events())
        layout.extend(self._build_markers())           # C5
        layout.extend(self._build_snapping_overlay())  # C1
        layout.extend(self._build_ghost_overlay())     # C2
        layout.extend(self._build_selection_overlay()) # C3

        return layout

    # ---------------------------------------------------------
    # Internal layout builders
    # ---------------------------------------------------------

    def _build_header(self) -> List[Dict[str, Any]]:
        blocks: List[Dict[str, Any]] = []

        blocks.append({
            "type": "text",
            "x": 0,
            "y": 0,
            "content": "Timeline",
        })

        for x in range(0, self.width, self.grid_step):
            blocks.append({
                "type": "text",
                "x": x,
                "y": 1,
                "content": f"{x}",
            })

        return blocks

    def _build_grid(self) -> List[Dict[str, Any]]:
        blocks: List[Dict[str, Any]] = []

        # Adaptive step
        if self.zoom < 0.75:
            step = self.grid_step * 2
        elif self.zoom > 1.5:
            step = max(2, self.grid_step // 2)
        else:
            step = self.grid_step

        for x in range(0, self.width, step):
            blocks.append({
                "type": "grid_line",
                "x": x,
                "y": 2,
                "height": self.height - 2,
            })

        return blocks

    def _build_events(self) -> List[Dict[str, Any]]:
        blocks: List[Dict[str, Any]] = []

        for ev in self._events:
            blocks.append({
                "type": "event",
                "x": ev["x"],
                "y": ev["y"],
                "width": ev["width"],
                "height": ev["height"],
                "label": ev["label"],
            })

        return blocks

    # ---------------------------------------------------------
    # C5 – Marker types
    # ---------------------------------------------------------

    def _build_markers(self) -> List[Dict[str, Any]]:
        blocks: List[Dict[str, Any]] = []

        for m in self._markers:
            blocks.append({
                "type": "marker",
                "x": m["x"],
                "y": m["y"],
                "icon": m["icon"],
                "label": m["label"],
                "color": m["color"],
            })

        return blocks

    # ---------------------------------------------------------
    # C1 – Snapping overlay
    # ---------------------------------------------------------

    def _build_snapping_overlay(self) -> List[Dict[str, Any]]:
        blocks: List[Dict[str, Any]] = []

        snapping_x = 30  # placeholder

        blocks.append({
            "type": "snapping_line",
            "x": snapping_x,
            "y": 2,
            "height": self.height - 2,
            "color": "cyan",
        })

        return blocks

    # ---------------------------------------------------------
    # C2 – Ghost dragging overlay
    # ---------------------------------------------------------

    def _build_ghost_overlay(self) -> List[Dict[str, Any]]:
        blocks: List[Dict[str, Any]] = []

        ghost_x = 25  # placeholder
        ghost_y = 4

        blocks.append({
            "type": "ghost_event",
            "x": ghost_x,
            "y": ghost_y,
            "width": 15,
            "height": 3,
            "opacity": 0.5,
            "label": "Ghost",
        })

        return blocks

    # ---------------------------------------------------------
    # C3 – Selection overlay
    # ---------------------------------------------------------

    def _build_selection_overlay(self) -> List[Dict[str, Any]]:
        blocks: List[Dict[str, Any]] = []

        sel = self._selected_event

        blocks.append({
            "type": "selection_box",
            "x": sel["x"],
            "y": sel["y"],
            "width": sel["width"],
            "height": sel["height"],
            "color": "yellow",
            "thickness": 1,
        })

        return blocks
