from dearpygui.core import *
from dearpygui.simple import *

from runtime.runtime_manager import RuntimeManager
from runtime.plugin_loader import PluginLoader
from runtime.nl_router import NaturalLanguageRouter


class SiriusGUI:
    """
    GUI front-end pre SIRIUS LOCAL AI ALFA – v2.0.0
    - prepojené s RuntimeManager 2.0
    - používa NL Router 2.0
    - podporuje AI tasky cez pluginy
    """

    def __init__(self):
        # --- BOOTSTRAP RUNTIME 2.0 ---
        self.runtime = RuntimeManager()
        self.runtime.initialize()

        # Pluginy
        self.plugins = PluginLoader(self.runtime)
        self.plugins.load_all()

        # NL Router 2.0
        self.router = NaturalLanguageRouter(self.runtime, self.plugins)
        self.router.initialize()

    # --------------------------------------------------------
    # GUI LOGIKA
    # --------------------------------------------------------
    def send_nl(self, sender, data):
        text = get_value("##input")
        if not text.strip():
            return

        result = self.router.route(text)

        add_text(f"> {text}", parent="Log")
        add_text(str(result), parent="Log")
        set_value("##input", "")

    def run_ai_task(self, sender, data):
        task_name = data.get("task")
        params = data.get("params", {})

        try:
            result = self.runtime.handle_ai_task(task_name, params)
        except Exception as e:
            result = f"Error: {e}"

        add_text(str(result), parent="Log")

    # --------------------------------------------------------
    # GUI OKNO
    # --------------------------------------------------------
    def run(self):
        with window("SIRIUS LOCAL AI – GUI", width=650, height=520):

            add_text("SIRIUS – Local AI Runtime (v2.0.0)")
            add_separator()

            add_input_text("##input", label="Command", width=450)
            add_button("Send", callback=self.send_nl)

            add_separator()
            add_text("Quick actions:")

            add_button("Snap VS Code Left",
                       callback=self.run_ai_task,
                       callback_data={"task": "snap_left", "params": {"app": "code.exe"}})

            add_button("Snap VS Code Right",
                       callback=self.run_ai_task,
                       callback_data={"task": "snap_right", "params": {"app": "code.exe"}})

            add_separator()
            add_text("Log:")
            add_child("Log", width=600, height=260)

        start_dearpygui()


# ------------------------------------------------------------
# SPÚŠŤACÍ BOD
# ------------------------------------------------------------
if __name__ == "__main__":
    gui = SiriusGUI()
    gui.run()
