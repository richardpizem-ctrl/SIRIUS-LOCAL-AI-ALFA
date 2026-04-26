# timeline_ui.py
# Core Timeline UI logic – generates layout blocks for PixelLayoutEngine
# SIRIUS LOCAL AI – timeline (Phase 4)

from typing import List, Dict, Any


class TimelineUI:
    """
    TimelineUI je logická vrstva časovej osi.
    Nevie nič o konkrétnom rendereri – generuje len layout bloky.

    V Phase 4 poskytuje:
        - základný grid
        - header
        - placeholder pre eventy
        - snapping overlay (C1)
        - pripravenú štruktúru pre ghost / selection
    """

    def __init__(self):
        self.width = 120
        self.height = 20
        self.grid_step = 10
        self._events = []  # neskôr: zoznam eventov na timeline

    # ---------------------------------------------------------
    # Public API
    # ---------------------------------------------------------

    def render(self) -> List[Dict[str, Any]]:
        """
        Hlavný vstupný bod – UI komponent volá render()
        a dostane list layout blokov.
        """
        layout: List[Dict[str, Any]] = []

        layout.extend(self._build_header())
        layout.extend(self._build_grid())
        layout.extend(self._build_events())
        layout.extend(self._build_snapping_overlay())  # C1

        # neskôr:
        # layout.extend(self._build_selection_overlay())
        # layout.extend(self._build_ghost_overlay())

        return layout

    # ---------------------------------------------------------
    # Internal layout builders
    # ---------------------------------------------------------

    def _build_header(self) -> List[Dict[str, Any]]:
        """
        Horný pás s časovými značkami.
        Zatiaľ jednoduchý textový header.
        """
        blocks: List[Dict[str, Any]] = []

        blocks.append({
            "type": "text",
            "x": 0,
            "y": 0,
            "content": "Timeline",
        })

        # Jednoduché značky každých grid_step
        for x in range(0, self.width, self.grid_step):
            blocks.append({
                "type": "text",
                "x": x,
                "y": 1,
                "content": f"{x}",
            })

        return blocks

    def _build_grid(self) -> List[Dict[str, Any]]:
        """
        Základný vertikálny grid pod headerom.
        """
        blocks: List[Dict[str, Any]] = []

        for x in range(0, self.width, self.grid_step):
            blocks.append({
                "type": "grid_line",
                "x": x,
                "y": 2,
                "height": self.height - 2,
            })

        return blocks

    def _build_events(self) -> List[Dict[str, Any]]:
        """
        Placeholder pre eventy na timeline.
        Neskôr sa napojí na reálne dáta.
        """
        blocks: List[Dict[str, Any]] = []

        # Placeholder – jeden demo event
        blocks.append({
            "type": "event",
            "x": 5,
            "y": 4,
            "width": 15,
            "height": 3,
            "label": "Demo event",
        })

        return blocks

    # ---------------------------------------------------------
    # C1 – Snapping overlay
    # ---------------------------------------------------------

    def _build_snapping_overlay(self) -> List[Dict[str, Any]]:
        """
        Vizualizácia snappingu – vertikálna čiara na pozícii,
        kde by sa event prilepil. Zatiaľ placeholder.
        """
        blocks: List[Dict[str, Any]] = []

        # Placeholder snapping position (neskôr dynamické)
        snapping_x = 30

        blocks.append({
            "type": "snapping_line",
            "x": snapping_x,
            "y": 2,
            "height": self.height - 2,
            "color": "cyan",
        })

        return blocks
