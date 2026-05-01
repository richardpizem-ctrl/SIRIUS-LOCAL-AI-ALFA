from dearpygui.core import *
from dearpygui.simple import *
from runtime.runtime_manager import RuntimeManager


class SiriusGUI:
    """
    Jednoduché GUI pre SIRIUS-LOCAL-AI
    - input na prirodzený jazyk
    - tlačidlá na AI tasky
    - log panel
    """

    def __init__(self):
        self.rm = RuntimeManager()
        self.rm.initialize()

    # --------------------------------------------------------
    # GUI LOGIKA
    # --------------------------------------------------------
    def send_nl(self, sender, data):
        text = get_value("##input")
        if not text.strip():
            return

        result = self.rm.handle_nl(text)
        add_text(f"> {text}", parent="Log")
        add_text(str(result), parent="Log")
        set_value("##input", "")

    def task_snap_left(self, sender, data):
        result = self.rm.handle_ai_task("snap_left", {"app": "code.exe"})
        add_text(str(result), parent="Log")

    def task_snap_right(self, sender, data):
        result = self.rm.handle_ai_task("snap_right", {"app": "code.exe"})
        add_text(str(result), parent="Log")

    # --------------------------------------------------------
    # GUI OKNO
    # --------------------------------------------------------
    def run(self):
        with window("SIRIUS-LOCAL-AI", width=600, height=500):

            add_text("SIRIUS – Local AI Runtime")
            add_separator()

            add_input_text("##input", label="Príkaz", width=400)
            add_button("Odoslať", callback=self.send_nl)

            add_separator()
            add_text("Rýchle akcie:")

            add_button("Daj VS Code doľava", callback=self.task_snap_left)
            add_button("Daj VS Code doprava", callback=self.task_snap_right)

            add_separator()
            add_text("Log:")
            add_child("Log", width=560, height=250)

        start_dearpygui()


# ------------------------------------------------------------
# SPÚŠŤACÍ BOD
# ------------------------------------------------------------
if __name__ == "__main__":
    gui = SiriusGUI()
    gui.run()
