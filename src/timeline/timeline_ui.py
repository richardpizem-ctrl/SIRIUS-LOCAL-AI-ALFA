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
        - marker lane (C6)
        - marker dragging overlay (C7)
    """

    def __init__(self):
        self.width = 120
        self.height = 20
        self.grid_step = 10
        self.zoom = 1.0  # C4 – placeholder zoom level

        # Marker lane height (C6)
        self.marker_lane_y = 2
        self.marker_lane_height = 1

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

        # C5 – Marker types
        self._markers = [
            {"x": 10, "icon": "🔵", "label": "Section Start", "color": "blue"},
            {"x": 40, "icon": "🟢", "label": "Loop Start", "color": "green"},
            {"x": 80, "icon": "🔴", "label": "Error", "color": "red"},
        ]

        # ---------------------------------------------------------
        # C7 – Marker dragging placeholder
        # ---------------------------------------------------------
        self._dragging_marker = {
            "active": True,      # placeholder: dragging is active
            "x": 55,             # ghost position
            "icon": "🟢",
            "label": "Loop Start",
            "color": "green",
        }

    # ---------------------------------------------------------
    # Public API
    # ---------------------------------------------------------

    def render(self) -> List[Dict[str, Any]]:
        layout: List[Dict[str, Any]] = []

        layout.extend(self._build_header())
        layout.extend(self._build_marker_lane())          # C6
        layout.extend(self._build_grid())                 # C4
        layout.extend(self._build_events())
        layout.extend(self._build_markers())              # C5
        layout.extend(self._build_marker_drag_overlay())  # C7
        layout.extend(self._build_snapping_overlay())     # C1
        layout.extend(self._build_ghost_overlay())        # C2
        layout.extend(self._build_selection_overlay())    # C3

        return layout

    # ---------------------------------------------------------
    # Internal layout builders
    # ---------------------------------------------------------

    def _build_header(self) -> List[Dict[str, Any]]:
        blocks: List[Dict[str, Any]] = []

        blocks.append({"type": "text", "x": 0, "y": 0, "content": "Timeline"})

        for x in range(0, self.width, self.grid_step):
            blocks.append({"type": "text", "x": x, "y": 1, "content": f"{x}"})

        return blocks

    # ---------------------------------------------------------
    # C6 – Marker lane
    # ---------------------------------------------------------

    def _build_marker_lane(self) -> List[Dict[str, Any]]:
        return [{
            "type": "marker_lane",
            "x": 0,
            "y": self.marker_lane_y,
            "width": self.width,
            "height": self.marker_lane_height,
            "color": "darkgray",
        }]

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
                "y": self.marker_lane_y + self.marker_lane_height,
                "height": self.height - (self.marker_lane_y + self.marker_lane_height),
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
                "y": self.marker_lane_y,
                "icon": m["icon"],
                "label": m["label"],
                "color": m["color"],
            })

        return blocks

    # ---------------------------------------------------------
    # C7 – Marker dragging overlay
    # ---------------------------------------------------------

    def _build_marker_drag_overlay(self) -> List[Dict[str, Any]]:
        """
        Vizualizácia ghost markeru počas ťahania.
        """
        blocks: List[Dict[str, Any]] = []

        if not self._dragging_marker["active"]:
            return blocks

        dm = self._dragging_marker

        blocks.append({
            "type": "marker_drag_ghost",
            "x": dm["x"],
            "y": self.marker_lane_y,
            "icon": dm["icon"],
            "label": dm["label"],
            "color": dm["color"],
            "opacity": 0.5,
        })

        return blocks

    # ---------------------------------------------------------
    # C1 – Snapping overlay
    # ---------------------------------------------------------

    def _build_snapping_overlay(self) -> List[Dict[str, Any]]:
        return [{
            "type": "snapping_line",
            "x": 30,
            "y": 2,
            "height": self.height - 2,
            "color": "cyan",
        }]

    # ---------------------------------------------------------
    # C2 – Ghost dragging overlay
    # ---------------------------------------------------------

    def _build_ghost_overlay(self) -> List[Dict[str, Any]]:
        return [{
            "type": "ghost_event",
            "x": 25,
            "y": 4,
            "width": 15,
            "height": 3,
            "opacity": 0.5,
            "label": "Ghost",
        }]

    # ---------------------------------------------------------
    # C3 – Selection overlay
    # ---------------------------------------------------------

    def _build_selection_overlay(self) -> List[Dict[str, Any]]:
        sel = self._selected_event

        return [{
            "type": "selection_box",
            "x": sel["x"],
            "y": sel["y"],
            "width": sel["width"],
            "height": sel["height"],
            "color": "yellow",
            "thickness": 1,
        }]
