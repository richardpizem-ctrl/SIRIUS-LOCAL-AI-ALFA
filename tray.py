import threading
import pystray
from pystray import MenuItem as Item
from PIL import Image, ImageDraw
import subprocess
import sys
import os


class SiriusTray:
    """
    Windows Tray ikonka pre SIRIUS-LOCAL-AI
    - otvára GUI
    - reštartuje runtime
    - vypína systém
    """

    def __init__(self):
        self.icon = pystray.Icon("SIRIUS", self._create_icon(), "SIRIUS-LOCAL-AI", self._menu())

    # --------------------------------------------------------
    # IKONA
    # --------------------------------------------------------
    def _create_icon(self):
        """
        Vytvorí jednoduchú čiernobielu ikonku (32x32).
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
            Item("Otvoriť GUI", self.open_gui),
            Item("Reštartovať runtime", self.restart_runtime),
            Item("Vypnúť SIRIUS", self.exit_app)
        )

    # --------------------------------------------------------
    # AKCIE
    # --------------------------------------------------------
    def open_gui(self, icon, item):
        """
        Spustí gui.py v novom procese.
        """
        python = sys.executable
        subprocess.Popen([python, "gui.py"])

    def restart_runtime(self, icon, item):
        """
        Reštartuje celý proces SIRIUS (jednoduchý spôsob).
        """
        python = sys.executable
        os.execv(python, [python] + sys.argv)

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
