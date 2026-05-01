def move_window(self, handle: int, x: int, y: int, width: int, height: int) -> bool:
    """
    Presunie a zmení veľkosť okna.
    - handle: HWND okna
    - x, y: nová pozícia
    - width, height: nové rozmery
    """
    try:
        import ctypes
        import ctypes.wintypes as wt

        user32 = ctypes.windll.user32

        # Overenie handle
        if not handle:
            log.warning("move_window called with invalid handle")
            return False

        # MoveWindow(handle, x, y, width, height, repaint=True)
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
