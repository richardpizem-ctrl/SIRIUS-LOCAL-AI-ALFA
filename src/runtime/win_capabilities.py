def focus_app_by_name(self, name: str) -> bool:
    """
    Zaostrí okno aplikácie podľa názvu (fuzzy match).
    - nájde okno podľa titulku
    - obnoví ho, ak je minimalizované
    - nastaví ho do popredia
    """
    try:
        import ctypes
        import ctypes.wintypes as wt

        user32 = ctypes.windll.user32

        # EnumWindows callback
        matches = []

        @ctypes.WINFUNCTYPE(ctypes.c_bool, wt.HWND, ctypes.c_void_p)
        def enum_callback(hwnd, lParam):
            # Získaj titulok okna
            length = user32.GetWindowTextLengthW(hwnd)
            if length == 0:
                return True  # žiadny titulok → ignoruj

            buffer = ctypes.create_unicode_buffer(length + 1)
            user32.GetWindowTextW(hwnd, buffer, length + 1)
            title = buffer.value

            # Fuzzy match (case-insensitive)
            if name.lower() in title.lower():
                matches.append((hwnd, title))

            return True

        # Prejdi všetky okná
        user32.EnumWindows(enum_callback, 0)

        if not matches:
            log.warning("No window found matching name: %s", name)
            return False

        # Vyber prvé najlepšie okno
        hwnd, title = matches[0]

        # Obnov okno, ak je minimalizované
        SW_RESTORE = 9
        user32.ShowWindow(hwnd, SW_RESTORE)

        # Nastav do popredia
        user32.SetForegroundWindow(hwnd)

        log.info("Focused window '%s' (hwnd=%s)", title, hwnd)
        return True

    except Exception as exc:
        log.exception("Failed to focus app by name: %s", exc)
        return False
