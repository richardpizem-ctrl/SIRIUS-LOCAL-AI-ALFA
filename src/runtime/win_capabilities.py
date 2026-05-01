def get_active_window(self) -> Optional[WindowInfo]:
    """
    Vráti informácie o aktuálne aktívnom okne:
    - handle
    - title
    - x, y, width, height
    """
    try:
        import ctypes
        import ctypes.wintypes as wt

        user32 = ctypes.windll.user32

        # 1. Získaj handle aktívneho okna
        hwnd = user32.GetForegroundWindow()
        if not hwnd:
            return None

        # 2. Získaj titulok okna
        length = user32.GetWindowTextLengthW(hwnd)
        buffer = ctypes.create_unicode_buffer(length + 1)
        user32.GetWindowTextW(hwnd, buffer, length + 1)
        title = buffer.value

        # 3. Získaj pozíciu a veľkosť okna
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


def snap_active_window_left(self) -> bool:
    """
    Zarovná aktívne okno na ľavú polovicu obrazovky.
    """
    try:
        import ctypes
        import ctypes.wintypes as wt

        user32 = ctypes.windll.user32

        # 1. Získaj aktívne okno
        hwnd = user32.GetForegroundWindow()
        if not hwnd:
            return False

        # 2. Získaj rozlíšenie obrazovky
        screen_width = user32.GetSystemMetrics(0)
        screen_height = user32.GetSystemMetrics(1)

        # 3. Presuň okno na ľavú polovicu
        user32.MoveWindow(hwnd, 0, 0, screen_width // 2, screen_height, True)
        return True

    except Exception as exc:
        log.exception("Failed to snap window left: %s", exc)
        return False


def snap_active_window_right(self) -> bool:
    """
    Zarovná aktívne okno na pravú polovicu obrazovky.
    """
    try:
        import ctypes
        import ctypes.wintypes as wt

        user32 = ctypes.windll.user32

        # 1. Získaj aktívne okno
        hwnd = user32.GetForegroundWindow()
        if not hwnd:
            return False

        # 2. Získaj rozlíšenie obrazovky
        screen_width = user32.GetSystemMetrics(0)
        screen_height = user32.GetSystemMetrics(1)

        # 3. Presuň okno na pravú polovicu
        user32.MoveWindow(hwnd, screen_width // 2, 0, screen_width // 2, screen_height, True)
        return True

    except Exception as exc:
        log.exception("Failed to snap window right: %s", exc)
        return False

