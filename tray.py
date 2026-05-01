import threading
import pystray
from pystray import MenuItem as Item
from PIL import Image, ImageDraw
import subprocess
import sys
import os
import pathlib


class SiriusTray:
    """
    Windows Tray ikonka pre SIRIUS LOCAL AI – v2.0.0
    - otvára GUI (cez python -m)
    - reštartuje celý SIRIUS runtime
    - vypína systém
    """

    def __init__(self):
        self.icon = pystray.Icon(
            "SIRIUS",
            self._create_icon(),
            "SIRIUS LOCAL AI",
            self._menu()
        )

    # --------------------------------------------------------
    # IKONA
    # --------------------------------------------------------
    def _create_icon(self):
        """
        Jednoduchá čiernobiela ikonka (32x32).
        """
        img = Image.new("RGB", (32, 32), "black")
        d = ImageDraw.Draw(img)
        d.rectangle([8, 8, 24, 24], fill="white")
        return img

    # --------------------------------------------------------
    # MENU
    # --------------------------------------------------------
    def _menu(self):
        return (
            Item("Open GUI", self.open_gui),
            Item("Restart SIRIUS", self.restart_sirius),
            Item("Exit Tray", self.exit_app)
        )

    # --------------------------------------------------------
    # AKCIE
    # --------------------------------------------------------
    def open_gui(self, icon, item):
        """
        Spustí GUI cez python -m, aby fungovalo aj pri rôznych cestách.
        """
        python = sys.executable

        # GUI modul v root priečinku
        gui_path = pathlib.Path(__file__).parent / "gui.py"

        subprocess.Popen([python, str(gui_path)])

    def restart_sirius(self, icon, item):
        """
        Reštartuje celý SIRIUS systém.
        Použije python -m sirius, aby sa spustil hlavný orchestrátor.
        """
        python = sys.executable

        # Hlavný orchestrátor sirius.py
        sirius_path = pathlib.Path(__file__).parent / "sirius.py"

        subprocess.Popen([python, str(sirius_path)])
        os._exit(0)

    def exit_app(self, icon, item):
        """
        Ukončí tray ikonku.
        """
        icon.stop()

    # --------------------------------------------------------
    # SPUSTENIE
    # --------------------------------------------------------
    def run(self):
        """
        Spustí tray ikonku v samostatnom vlákne.
        """
        threading.Thread(target=self.icon.run, daemon=True).start()


# ------------------------------------------------------------
# SPÚŠŤACÍ BOD
# ------------------------------------------------------------
if __name__ == "__main__":
    tray = SiriusTray()
    tray.run()

    # Tray beží na pozadí → hlavné vlákno musí zostať živé
    try:
        while True:
            pass
    except KeyboardInterrupt:
        pass
