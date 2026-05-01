"""
win_capabilities.py

Windows Capabilities Layer (WIN-CAP) for SIRIUS-LOCAL-AI-ALFA.

Zodpovednosť:
- Poskytuje bezpečné, vysokoúrovňové API na prácu so schopnosťami Windows 11:
  - aplikácie
  - okná
  - súborový systém (len ne-deštruktívne operácie)
  - audio zariadenia
  - systémový kontext

Poznámka:
- Tento modul NEVYKONÁVA žiadne akcie sám od seba.
- Všetky volania musia byť sprostredkované cez vyššiu vrstvu (CME / UI Confirm).
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional, Dict, Any

import sys
import logging

log = logging.getLogger(__name__)


# ──────────────────────────────────────────────────────────────────────────────
# Platform guard
# ──────────────────────────────────────────────────────────────────────────────

def _ensure_windows() -> None:
    if sys.platform != "win32":
        raise RuntimeError("WIN-CAP is only available on Windows (win32).")


# ──────────────────────────────────────────────────────────────────────────────
# Data models
# ──────────────────────────────────────────────────────────────────────────────

@dataclass
class RunningApp:
    name: str
    pid: int
    main_window_title: str


@dataclass
class WindowInfo:
    handle: int
    title: str
    x: int
    y: int
    width: int
    height: int


@dataclass
class AudioDevice:
    id: str
    name: str
    is_default: bool


@dataclass
class SystemState:
    active_window_title: Optional[str]
    active_app_name: Optional[str]
    mounted_drives: List[str]


# ──────────────────────────────────────────────────────────────────────────────
# Core class
# ──────────────────────────────────────────────────────────────────────────────

class WinCapabilities:
    """
    High-level Windows capabilities wrapper.

    Tento modul je navrhnutý tak, aby:
    - bol volaný z runtime (CME / workflow)
    - neobsahoval žiadnu UI logiku
    - bol deterministický a predvídateľný
    """

    def __init__(self) -> None:
        _ensure_windows()
        # TODO: lazy init pre konkrétne subsystémy (win32 API, audio, atď.)
        log.debug("WinCapabilities initialized")

    # ──────────────────────────────────────────────────────────────────────
    # Applications
    # ──────────────────────────────────────────────────────────────────────

    def list_running_apps(self) -> List[RunningApp]:
        """
        Vráti zoznam bežiacich aplikácií.

        TODO:
        - použiť psutil alebo win32 API (EnumWindows + GetWindowThreadProcessId)
        """
        log.debug("Listing running applications")
        # placeholder
        return []

    def open_app(self, path: str, args: Optional[List[str]] = None) -> bool:
        """
        Spustí aplikáciu na danej ceste.

        - path: absolútna cesta k .exe alebo asociovanému súboru
        - args: voliteľné argumenty

        TODO:
        - použiť subprocess / os.startfile
        - validácia cesty (FS-AGENT by mal byť upstream)
        """
        log.info("Request to open app: path=%s args=%s", path, args)
        try:
            import subprocess
            cmd = [path] + (args or [])
            subprocess.Popen(cmd)
            return True
        except Exception as exc:
            log.exception("Failed to open app: %s", exc)
            return False

    def focus_app_by_name(self, name: str) -> bool:
        """
        Zaostrí okno aplikácie podľa mena.

        TODO:
        - win32gui.EnumWindows + SetForegroundWindow
        - fuzzy match podľa title / process name
        """
        log.info("Request to focus app by name: %s", name)
        # placeholder
        return False

    # ──────────────────────────────────────────────────────────────────────
    # Windows
    # ──────────────────────────────────────────────────────────────────────

    def get_active_window(self) -> Optional[WindowInfo]:
        """
        Vráti informácie o aktuálne aktívnom okne.

        TODO:
        - GetForegroundWindow + GetWindowRect + GetWindowText
        """
        log.debug("Getting active window info")
        # placeholder
        return None

    def snap_active_window_left(self) -> bool:
        """
        Zarovná aktívne okno na ľavú polovicu obrazovky.

        TODO:
        - použiť GetForegroundWindow + MoveWindow / SetWindowPos
        - získať rozlíšenie obrazovky (GetSystemMetrics)
        """
        log.info("Request to snap active window left")
        # placeholder
        return False

    def snap_active_window_right(self) -> bool:
        """
        Zarovná aktívne okno na pravú polovicu obrazovky.
        """
        log.info("Request to snap active window right")
        # placeholder
        return False

    def move_window(self, handle: int, x: int, y: int, width: int, height: int) -> bool:
        """
        Presunie a zmení veľkosť okna.

        TODO:
        - MoveWindow(handle, x, y, width, height, True)
        """
        log.info(
            "Request to move window: handle=%s x=%s y=%s w=%s h=%s",
            handle, x, y, width, height
        )
        # placeholder
        return False

    # ──────────────────────────────────────────────────────────────────────
    # Audio devices
    # ──────────────────────────────────────────────────────────────────────

    def list_audio_devices(self) -> List[AudioDevice]:
        """
        Vráti zoznam audio zariadení.

        TODO:
        - použiť napr. pycaw / WASAPI
        """
        log.debug("Listing audio devices")
        # placeholder
        return []

    def get_active_audio_device(self) -> Optional[AudioDevice]:
        """
        Vráti aktuálne predvolené audio zariadenie.
        """
        log.debug("Getting active audio device")
        devices = self.list_audio_devices()
        for dev in devices:
            if dev.is_default:
                return dev
        return None

    def switch_audio_device(self, name: str) -> bool:
        """
        Prepne predvolené audio zariadenie podľa mena.

        TODO:
        - WASAPI / pycaw / externý helper
        """
        log.info("Request to switch audio device to: %s", name)
        # placeholder
        return False

    # ──────────────────────────────────────────────────────────────────────
    # System context
    # ──────────────────────────────────────────────────────────────────────

    def get_system_state(self) -> SystemState:
        """
        Vráti základný systémový kontext:
        - aktívne okno
        - aktívna aplikácia (ak vieme odvodiť)
        - pripojené disky
        """
        log.debug("Collecting system state")
        active_window = self.get_active_window()
        mounted_drives = self._list_mounted_drives()

        return SystemState(
            active_window_title=active_window.title if active_window else None,
            active_app_name=None,  # TODO: odvodiť z PID / process name
            mounted_drives=mounted_drives,
        )

    def _list_mounted_drives(self) -> List[str]:
        """
        Vráti zoznam písmen diskov.

        TODO:
        - použiť win32api.GetLogicalDriveStrings alebo pathlib / os
        """
        log.debug("Listing mounted drives")
        try:
            import string
            import os

            drives: List[str] = []
            for letter in string.ascii_uppercase:
                path = f"{letter}:\\"
                if os.path.exists(path):
                    drives.append(path)
            return drives
        except Exception as exc:
            log.exception("Failed to list drives: %s", exc)
            return []

    # ──────────────────────────────────────────────────────────────────────
    # Project / folder utilities (non-destructive)
    # ──────────────────────────────────────────────────────────────────────

    def find_projects(self, root_paths: List[str]) -> List[str]:
        """
        Nájde projekty (napr. SIRIUS, Git repozitáre) v daných koreňových cestách.

        TODO:
        - hľadať podľa markerov (.git, specific files)
        - rešpektovať FS-AGENT pre bezpečné prechádzanie
        """
        log.info("Request to find projects in: %s", root_paths)
        # placeholder
        return []

    def prepare_folder_structure(self, base_path: str, structure: Dict[str, Any]) -> bool:
        """
        Pripraví priečinkovú štruktúru pre nový projekt / verziu.

        - base_path: koreňový priečinok
        - structure: definícia štruktúry (napr. { "docs": {}, "src": {"runtime": {}} })

        TODO:
        - delegovať na FS-AGENT (tento modul by nemal vytvárať priečinky priamo)
        """
        log.info("Request to prepare folder structure at: %s", base_path)
        # placeholder
        return False
