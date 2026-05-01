import os
import ctypes
import ctypes.wintypes as wt
from typing import List, Optional, Dict, Any
from dataclasses import dataclass
import logging

log = logging.getLogger(__name__)


# ------------------------------------------------------------
# DATA STRUCTURES
# ------------------------------------------------------------

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


# ------------------------------------------------------------
# WIN-CAPABILITIES LAYER
# ------------------------------------------------------------

class WinCapabilities:

    # --------------------------------------------------------
    # ACTIVE WINDOW
    # --------------------------------------------------------
    def get_active_window(self) -> Optional[WindowInfo]:
        try:
            user32 = ctypes.windll.user32

            hwnd = user32.GetForegroundWindow()
            if not hwnd:
                return None

            length = user32.GetWindowTextLengthW(hwnd)
            buffer = ctypes.create_unicode_buffer(length + 1)
            user32.GetWindowTextW(hwnd, buffer, length + 1)
            title = buffer.value

            rect = wt.RECT()
            user32.GetWindowRect(hwnd, ctypes.byref(rect))

            x = rect.left
            y = rect.top
            width = rect.right - rect.left
            height = rect.bottom - rect.top

            return WindowInfo(
                handle=hwnd,
                title=title,
                x=x,
                y=y,
                width=width,
                height=height
            )

        except Exception as exc:
            log.exception("Failed to get active window: %s", exc)
            return None

    # --------------------------------------------------------
    # WINDOW SNAPPING
    # --------------------------------------------------------
    def snap_active_window_left(self) -> bool:
        try:
            user32 = ctypes.windll.user32

            hwnd = user32.GetForegroundWindow()
            if not hwnd:
                return False

            screen_width = user32.GetSystemMetrics(0)
            screen_height = user32.GetSystemMetrics(1)

            user32.MoveWindow(hwnd, 0, 0, screen_width // 2, screen_height, True)
            return True

        except Exception as exc:
            log.exception("Failed to snap window left: %s", exc)
            return False

    def snap_active_window_right(self) -> bool:
        try:
            user32 = ctypes.windll.user32

            hwnd = user32.GetForegroundWindow()
            if not hwnd:
                return False

            screen_width = user32.GetSystemMetrics(0)
            screen_height = user32.GetSystemMetrics(1)

            user32.MoveWindow(hwnd, screen_width // 2, 0, screen_width // 2, screen_height, True)
            return True

        except Exception as exc:
            log.exception("Failed to snap window right: %s", exc)
            return False

    # --------------------------------------------------------
    # WINDOW MOVE
    # --------------------------------------------------------
    def move_window(self, handle: int, x: int, y: int, width: int, height: int) -> bool:
        try:
            user32 = ctypes.windll.user32

            if not handle:
                log.warning("move_window called with invalid handle")
                return False

            success = user32.MoveWindow(handle, x, y, width, height, True)

            if success:
                log.info(
                    "Moved window (hwnd=%s) to x=%s y=%s w=%s h=%s",
                    handle, x, y, width, height
                )
                return True
            else:
                log.error("MoveWindow failed for hwnd=%s", handle)
                return False

        except Exception as exc:
            log.exception("Failed to move window: %s", exc)
            return False

    # --------------------------------------------------------
    # FOCUS APP BY NAME
    # --------------------------------------------------------
    def focus_app_by_name(self, name: str) -> bool:
        try:
            user32 = ctypes.windll.user32
            matches = []

            @ctypes.WINFUNCTYPE(ctypes.c_bool, wt.HWND, ctypes.c_void_p)
            def enum_callback(hwnd, lParam):
                length = user32.GetWindowTextLengthW(hwnd)
                if length == 0:
                    return True

                buffer = ctypes.create_unicode_buffer(length + 1)
                user32.GetWindowTextW(hwnd, buffer, length + 1)
                title = buffer.value

                if name.lower() in title.lower():
                    matches.append((hwnd, title))

                return True

            user32.EnumWindows(enum_callback, 0)

            if not matches:
                log.warning("No window found matching name: %s", name)
                return False

            hwnd, title = matches[0]

            SW_RESTORE = 9
            user32.ShowWindow(hwnd, SW_RESTORE)
            user32.SetForegroundWindow(hwnd)

            log.info("Focused window '%s' (hwnd=%s)", title, hwnd)
            return True

        except Exception as exc:
            log.exception("Failed to focus app by name: %s", exc)
            return False

    # --------------------------------------------------------
    # AUDIO DEVICES
    # --------------------------------------------------------
    def list_audio_devices(self) -> List[AudioDevice]:
        try:
            import ctypes
            from ctypes import POINTER
            from ctypes.wintypes import DWORD

            CLSCTX_ALL = 23

            class IMMDeviceEnumerator(ctypes.c_void_p):
                pass

            class IMMDevice(ctypes.c_void_p):
                pass

            class IPropertyStore(ctypes.c_void_p):
                pass

            CLSID_MMDeviceEnumerator = ctypes.c_char_p(
                b"{BCDE0395-E52F-467C-8E3D-C4579291692E}"
            )
            IID_IMMDeviceEnumerator = ctypes.c_char_p(
                b"{A95664D2-9614-4F35-A746-DE8DB63617E6}"
            )

            ole32 = ctypes.windll.ole32
            ole32.CoInitialize(None)

            enumerator = POINTER(IMMDeviceEnumerator)()
            ole32.CoCreateInstance(
                CLSID_MMDeviceEnumerator,
                None,
                CLSCTX_ALL,
                IID_IMMDeviceEnumerator,
                ctypes.byref(enumerator)
            )

            default_device = POINTER(IMMDevice)()
            enumerator.GetDefaultAudioEndpoint(0, 1, ctypes.byref(default_device))

            property_store = POINTER(IPropertyStore)()
            default_device.OpenPropertyStore(0, ctypes.byref(property_store))

            class PROPERTYKEY(ctypes.Structure):
                _fields_ = [
                    ("fmtid", ctypes.c_byte * 16),
                    ("pid", DWORD),
                ]

            PKEY_Device_FriendlyName = PROPERTYKEY(
                (0xA4, 0x41, 0x4F, 0xC6, 0xE4, 0xD8, 0x4A, 0xD1,
                 0x87, 0xB6, 0xE0, 0xDB, 0xEF, 0xE3, 0x5A, 0xA5),
                14
            )

            class PROPVARIANT(ctypes.Structure):
                _fields_ = [
                    ("vt", ctypes.c_ushort),
                    ("wReserved1", ctypes.c_ubyte),
                    ("wReserved2", ctypes.c_ubyte),
                    ("wReserved3", DWORD),
                    ("pszVal", ctypes.c_wchar_p),
                ]

            prop = PROPVARIANT()
            property_store.GetValue(ctypes.byref(PKEY_Device_FriendlyName), ctypes.byref(prop))

            device_name = prop.pszVal

            return [
                AudioDevice(
                    id="default",
                    name=device_name,
                    is_default=True
                )
            ]

        except Exception as exc:
            log.exception("Failed to list audio devices: %s", exc)
            return []

    # --------------------------------------------------------
    # SYSTEM CONTEXT
    # --------------------------------------------------------
    def _list_mounted_drives(self) -> List[str]:
        try:
            import string
            drives = []
            for letter in string.ascii_uppercase:
                path = f"{letter}:\\"
                if os.path.exists(path):
                    drives.append(path)
            return drives
        except Exception as exc:
            log.exception("Failed to list drives: %s", exc)
            return []

    def get_system_state(self) -> SystemState:
        log.debug("Collecting system state")

        active_window = self.get_active_window()
        mounted_drives = self._list_mounted_drives()

        active_app_name = active_window.title if active_window else None

        return SystemState(
            active_window_title=active_window.title if active_window else None,
            active_app_name=active_app_name,
            mounted_drives=mounted_drives,
        )

    # --------------------------------------------------------
    # PROJECT UTILITIES
    # --------------------------------------------------------
    def find_projects(self, root_paths: List[str]) -> List[str]:
        log.info("Searching for projects in: %s", root_paths)

        markers = [
            ".git",
            "pyproject.toml",
            "sirius.json",
        ]

        found = []

        try:
            for root in root_paths:
                if not os.path.exists(root):
                    continue

                for dirpath, dirnames, filenames in os.walk(root):
                    for marker in markers:
                        if marker in dirnames or marker in filenames:
                            found.append(dirpath)
                            break

            return found

        except Exception as exc:
            log.exception("Failed to search for projects: %s", exc)
            return []

    def prepare_folder_structure(self, base_path: str, structure: Dict[str, Any]) -> bool:
        try:
            plan = []

            def walk(path: str, subtree: Dict[str, Any]):
                for name, content in subtree.items():
                    full = f"{path}/{name}"
                    plan.append(full)
                    if isinstance(content, dict):
                        walk(full, content)

            walk(base_path, structure)

            log.info("Prepared folder structure plan: %s", plan)

            self._pending_folder_plan = plan
            return True

        except Exception as exc:
            log.exception("Failed to prepare folder structure: %s", exc)
            return False


# ------------------------------------------------------------
# COMMAND MEDIATION ENGINE (CME)
# ------------------------------------------------------------

class CommandMediationEngine:
    """
    CME = Command Mediation Engine
    - prijíma príkazy od AI
    - rozhoduje, či treba potvrdenie
    - vykonáva cez WinCapabilities
    - loguje a chráni systém
    """

    def __init__(self):
        self.win = WinCapabilities()

    def execute(self, command: str, args: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        log.info("CME received command: %s args=%s", command, args)

        try:
            if command == "snap_left":
                return self._wrap(self.win.snap_active_window_left())

            if command == "snap_right":
                return self._wrap(self.win.snap_active_window_right())

            if command == "focus_app":
                return self._wrap(self.win.focus_app_by_name(args["name"]))

            if command == "move_window":
                return self._wrap(self.win.move_window(
                    handle=args["handle"],
                    x=args["x"],
                    y=args["y"],
                    width=args["width"],
                    height=args["height"]
                ))

            if command == "list_audio_devices":
                devices = self.win.list_audio_devices()
                return {"ok": True, "devices": [d.__dict__ for d in devices]}

            if command == "system_state":
                state = self.win.get_system_state()
                return {"ok": True, "state": state.__dict__}

            if command == "find_projects":
                projects = self.win.find_projects(args["roots"])
                return {"ok": True, "projects": projects}

            if command == "prepare_structure":
                ok = self.win.prepare_folder_structure(args["base"], args["structure"])
                return self._wrap(ok)

            log.warning("Unknown command: %s", command)
            return {"ok": False, "error": "Unknown command"}

        except Exception as exc:
            log.exception("CME failed: %s", exc)
            return {"ok": False, "error": str(exc)}

    def _wrap(self, result: bool) -> Dict[str, Any]:
        return {"ok": bool(result)}


# ------------------------------------------------------------
# UI CONFIRM LAYER
# ------------------------------------------------------------

class UIConfirm:
    """
    UI Confirm Layer
    - zachytáva nebezpečné alebo systémové príkazy
    - vyžaduje potvrdenie od používateľa
    - integruje sa s CME
    """

    def __init__(self, cme: CommandMediationEngine):
        self.cme = cme

        self.confirm_required = {
            "move_window",
            "prepare_structure",
            "delete_file",
            "delete_folder",
            "switch_audio_device",
        }

    def request(self, command: str, args: Dict[str, Any]) -> Dict[str, Any]:
        if command in self.confirm_required:
            return self._build_confirmation(command, args)

        return self.cme.execute(command, args)

    def _build_confirmation(self, command: str, args: Dict[str, Any]) -> Dict[str, Any]:
        return {
            "requires_confirmation": True,
            "command": command,
            "args": args,
            "message": self._describe(command, args),
            "options": ["ANO", "NIE"]
        }

    def _describe(self, command: str, args: Dict[str, Any]) -> str:
        if command == "move_window":
            return (
                f"Chceš presunúť okno (hwnd={args['handle']}) "
                f"na x={args['x']}, y={args['y']} "
                f"a veľkosť {args['width']}×{args['height']}?"
            )

        if command == "prepare_structure":
            return (
                f"Chceš pripraviť priečinkovú štruktúru v '{args['base']}' "
                f"({len(args['structure'])} položiek)?"
            )

        if command == "switch_audio_device":
            return f"Chceš prepínať audio zariadenie na '{args['name']}'?"

        if command == "delete_file":
            return f"Chceš odstrániť súbor '{args['path']}'?"

        if command == "delete_folder":
            return f"Chceš odstrániť priečinok '{args['path']}'?"

        return f"Chceš vykonať príkaz '{command}'?"

    def confirm(self, command: str, args: Dict[str, Any], answer: str) -> Dict[str, Any]:
        if answer.upper() != "ANO":
            return {"ok": False, "cancelled": True}

        return self.cme.execute(command, args)


# ------------------------------------------------------------
# WORKFLOW ENGINE 2.0
# ------------------------------------------------------------

class WorkflowEngine:
    """
    Workflow Engine 2.0
    - skladá jednoduché príkazy do workflowov
    - používa UIConfirm + CME + WinCapabilities
    - poskytuje vysokú úroveň akcií typu:
      - 'daj VS Code doprava'
      - 'otvor projekt a zaostri okno'
      - 'priprav štruktúru pre release'
    """

    def __init__(self):
        self.cme = CommandMediationEngine()
        self.ui = UIConfirm(self.cme)

    # --------------------------------------------------------
    # VYSOKOÚROVŇOVÉ WORKFLOWY
    # --------------------------------------------------------

    def snap_app_right(self, app_name: str) -> Dict[str, Any]:
        """
        Workflow:
        1) Zaostri app podľa názvu
        2) Snap doprava
        """
        focus = self.cme.execute("focus_app", {"name": app_name})
        if not focus.get("ok"):
            return {"ok": False, "step": "focus_app", "error": focus.get("error")}

        snap = self.cme.execute("snap_right", {})
        if not snap.get("ok"):
            return {"ok": False, "step": "snap_right", "error": snap.get("error")}

        return {"ok": True}

    def open_project_and_focus(self, project_root: str, app_name: str) -> Dict[str, Any]:
        """
        Workflow:
        1) Over projekt
        2) Zaostri app
        """
        projects = self.cme.execute("find_projects", {"roots": [project_root]})
        if not projects.get("ok") or not projects.get("projects"):
            return {"ok": False, "step": "find_projects", "error": "Project not found"}

        focus = self.cme.execute("focus_app", {"name": app_name})
        if not focus.get("ok"):
            return {"ok": False, "step": "focus_app", "error": focus.get("error")}

        return {"ok": True}

    def prepare_release_structure(self, base_path: str, structure: Dict[str, Any]) -> Dict[str, Any]:
        """
        Workflow:
        1) Požiadať o potvrdenie (UIConfirm)
        2) Po potvrdení spustiť prepare_structure cez CME
        """
        request = self.ui.request("prepare_structure", {"base": base_path, "structure": structure})

        if request.get("requires_confirmation"):
            return request  # UI zobrazí otázku

        return request

    def confirm_and_execute(self, payload: Dict[str, Any], answer: str) -> Dict[str, Any]:
        """
        Používateľ odpovie ANO/NIE.
        """
        if not payload.get("requires_confirmation"):
            return {"ok": False, "error": "Nothing to confirm"}

        return self.ui.confirm(payload["command"], payload["args"], answer)
