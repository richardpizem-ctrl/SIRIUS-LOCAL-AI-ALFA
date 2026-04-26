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
        - event dragging overlay (C8)
        - event resize overlay (C9)
        - hover overlay (C10)
        - grid hover overlay (C11)
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
            {"x": 5, "y": 4, "width": 15, "height": 3, "label": "Demo event"}
        ]

        # Placeholder vybraný event (C3)
        self._selected_event = {"x": 5, "y": 4, "width": 15, "height": 3}

        # C5 – Marker types
        self._markers = [
            {"x": 10, "icon": "🔵", "label": "Section Start", "color": "blue"},
            {"x": 40, "icon": "🟢", "label": "Loop Start", "color": "green"},
            {"x": 80, "icon": "🔴", "label": "Error", "color": "red"},
        ]

        # C7 – Marker dragging placeholder
        self._dragging_marker = {
            "active": True,
            "x": 55,
            "icon": "🟢",
            "label": "Loop Start",
            "color": "green",
        }

        # C8 – Event dragging placeholder
        self._dragging_event = {
            "active": True,
            "x": 35,
            "y": 4,
            "width": 15,
            "height": 3,
            "label": "Dragging Event",
        }

        # C9 – Event resize placeholder
        self._resizing_event = {
            "active": True,
            "x": 5,
            "y": 4,
            "width": 20,
            "height": 3,
            "label": "Resizing Event",
            "handle": "right",
        }

        # C10 – Hover overlay placeholder
        self._hover = {
            "active": True,
            "x": 5,
            "y": 4,
            "width": 15,
            "height": 3,
            "color": "white",
        }

        # ---------------------------------------------------------
        # C11 – Grid hover placeholder
        # ---------------------------------------------------------
        self._grid_hover = {
            "active": True,
            "x": 30,
            "width": 10,
            "color": "lightblue",
        }

    # ---------------------------------------------------------
    # Public API
    # ---------------------------------------------------------

    def render(self) -> List[Dict[str, Any]]:
        layout: List[Dict[str, Any]] = []

        layout.extend(self._build_header())
        layout.extend(self._build_marker_lane())          # C6
        layout.extend(self._build_grid())                 # C4
        layout.extend(self._build_grid_hover_overlay())   # C11
        layout.extend(self._build_events())
        layout.extend(self._build_event_drag_overlay())   # C8
        layout.extend(self._build_event_resize_overlay()) # C9
        layout.extend(self._build_hover_overlay())        # C10
        layout.extend(self._build_markers())              # C5
        layout.extend(self._build_marker_drag_overlay())  # C7
        layout.extend(self._build_snapping_overlay())     # C1
        layout.extend(self._build_ghost_overlay())        # C2
        layout.extend(self._build_selection_overlay())    # C3

        return layout

    # ---------------------------------------------------------
    # Internal layout builders
    # ---------------------------------------------------------

    def _build_header(self):
        blocks = [{"type": "text", "x": 0, "y": 0, "content": "Timeline"}]

        for x in range(0, self.width, self.grid_step):
            blocks.append({"type": "text", "x": x, "y": 1, "content": f"{x}"})

        return blocks

    # C6 – Marker lane
    def _build_marker_lane(self):
        return [{
            "type": "marker_lane",
            "x": 0,
            "y": self.marker_lane_y,
            "width": self.width,
            "height": self.marker_lane_height,
            "color": "darkgray",
        }]

    # C4 – Adaptive grid
    def _build_grid(self):
        blocks = []

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

    # ---------------------------------------------------------
    # C11 – Grid hover overlay
    # ---------------------------------------------------------

    def _build_grid_hover_overlay(self):
        blocks = []

        if not self._grid_hover["active"]:
            return blocks

        gh = self._grid_hover

        blocks.append({
            "type": "grid_hover",
            "x": gh["x"],
            "y": self.marker_lane_y + self.marker_lane_height,
            "width": gh["width"],
            "height": self.height - (self.marker_lane_y + self.marker_lane_height),
            "color": gh["color"],
            "opacity": 0.2,
        })

        return blocks

    # Events
    def _build_events(self):
        blocks = []

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

    # C8 – Event dragging overlay
    def _build_event_drag_overlay(self):
        if not self._dragging_event["active"]:
            return []

        de = self._dragging_event

        return [{
            "type": "event_drag_ghost",
            "x": de["x"],
            "y": de["y"],
            "width": de["width"],
            "height": de["height"],
            "opacity": 0.5,
            "label": de["label"],
        }]

    # C9 – Event resize overlay
    def _build_event_resize_overlay(self):
        if not self._resizing_event["active"]:
            return []

        re = self._resizing_event

        blocks = [{
            "type": "event_resize_ghost",
            "x": re["x"],
            "y": re["y"],
            "width": re["width"],
            "height": re["height"],
            "opacity": 0.5,
            "label": re["label"],
        }]

        handle_x = re["x"] + re["width"] if re["handle"] == "right" else re["x"]

        blocks.append({
            "type": "resize_handle",
            "x": handle_x,
            "y": re["y"],
            "height": re["height"],
            "color": "orange",
        })

        return blocks

    # C10 – Hover overlay
    def _build_hover_overlay(self):
        if not self._hover["active"]:
            return []

        h = self._hover

        return [{
            "type": "hover_box",
            "x": h["x"],
            "y": h["y"],
            "width": h["width"],
            "height": h["height"],
            "color": h["color"],
            "opacity": 0.3,
        }]

    # C5 – Marker types
    def _build_markers(self):
        blocks = []

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

    # C7 – Marker dragging overlay
    def _build_marker_drag_overlay(self):
        if not self._dragging_marker["active"]:
            return []

        dm = self._dragging_marker

        return [{
            "type": "marker_drag_ghost",
            "x": dm["x"],
            "y": self.marker_lane_y,
            "icon": dm["icon"],
            "label": dm["label"],
            "color": dm["color"],
            "opacity": 0.5,
        }]

    # C1 – Snapping overlay
    def _build_snapping_overlay(self):
        return [{
            "type": "snapping_line",
            "x": 30,
            "y": 2,
            "height": self.height - 2,
            "color": "cyan",
        }]

    # C2 – Ghost dragging overlay
    def _build_ghost_overlay(self):
        return [{
            "type": "ghost_event",
            "x": 25,
            "y": 4,
            "width": 15,
            "height": 3,
            "opacity": 0.5,
            "label": "Ghost",
        }]

    # C3 – Selection overlay
    def _build_selection_overlay(self):
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
