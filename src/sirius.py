"""
SIRIUS LOCAL AI ALFA – v2.0.0 entrypoint

Toto je hlavný spúšťací bod pre SIRIUS 2.0 runtime.
– bootstrap RuntimeManager 2.0
– načítanie pluginov cez PluginLoader 2.0
– inicializácia NL Router 2.0
– spustenie AI Loop 2.0 (autonómny režim)
– CLI režim ako základný front-end
– hooky pre GUI / TRAY / VOICE (budúce moduly)
"""

import argparse
import threading
import sys
from typing import Optional

# --- CORE RUNTIME 2.0 ---

from runtime.runtime_manager import RuntimeManager
from runtime.plugin_loader import PluginLoader
from runtime.nl_router import NaturalLanguageRouter
from runtime.ai_loop import AILoop


class SiriusApp:
    """
    Hlavná aplikačná trieda, ktorá orchestruje celý SIRIUS runtime.
    """

    def __init__(self, enable_ai_loop: bool = True) -> None:
        # Runtime core
        self.runtime = RuntimeManager()

        # Plugin system
        self.plugin_loader = PluginLoader(self.runtime)

        # Natural language router
        self.nl_router = NaturalLanguageRouter(self.runtime, self.plugin_loader)

        # Autonómny AI loop
        self.ai_loop: Optional[AILoop] = None
        if enable_ai_loop:
            self.ai_loop = AILoop(self.runtime, self.plugin_loader)

        self._ai_loop_thread: Optional[threading.Thread] = None

    # --------------------------------------------------------------------- #
    #  BOOTSTRAP
    # --------------------------------------------------------------------- #

    def bootstrap(self) -> None:
        """
        Inicializuje runtime, načíta pluginy a pripraví systém na použitie.
        """
        # 1) Inicializácia runtime
        self.runtime.initialize()

        # 2) Načítanie pluginov
        self.plugin_loader.load_all()

        # 3) Inicializácia NL routera
        self.nl_router.initialize()

        # 4) Spustenie AI loop (ak je zapnutý)
        if self.ai_loop is not None:
            self._start_ai_loop_background()

    def _start_ai_loop_background(self) -> None:
        """
        Spustí AI loop v samostatnom vlákne (autonómny režim).
        """
        if self.ai_loop is None:
            return

        def _runner() -> None:
            try:
                self.ai_loop.run()
            except Exception as e:
                # Runtime by mal mať vlastný logging, tu len fallback
                self.runtime.log_error(f"AI Loop crashed: {e}")

        self._ai_loop_thread = threading.Thread(
            target=_runner,
            name="SIRIUS-AI-LOOP",
            daemon=True,
        )
        self._ai_loop_thread.start()

    # --------------------------------------------------------------------- #
    #  FRONT-END HOOKS
    # --------------------------------------------------------------------- #

    def handle_text(self, text: str) -> str:
        """
        Spracuje textový vstup (CLI, GUI, VOICE) cez NL Router 2.0.
        """
        text = text.strip()
        if not text:
            return ""

        try:
            return self.nl_router.route(text)
        except Exception as e:
            self.runtime.log_error(f"Error while handling input: {e}")
            return f"Error: {e}"

    # --------------------------------------------------------------------- #
    #  CLI REŽIM
    # --------------------------------------------------------------------- #

    def run_cli(self) -> None:
        """
        Jednoduchý konzolový režim – základný front-end pre SIRIUS 2.0.
        """
        print("SIRIUS LOCAL AI ALFA – v2.0.0 (Runtime 2.0)")
        print("Type 'exit' to quit.\n")

        while True:
            try:
                user_input = input(">>> ").strip()
            except (EOFError, KeyboardInterrupt):
                print("\nExiting SIRIUS.")
                break

            if user_input.lower() in {"exit", "quit"}:
                print("Exiting SIRIUS.")
                break

            if not user_input:
                continue

            output = self.handle_text(user_input)
            if output:
                print(output)

    # --------------------------------------------------------------------- #
    #  SHUTDOWN
    # --------------------------------------------------------------------- #

    def shutdown(self) -> None:
        """
        Korektné ukončenie runtime a AI loop.
        """
        if self.ai_loop is not None:
            try:
                self.ai_loop.stop()
            except Exception:
                pass

        if self._ai_loop_thread is not None and self._ai_loop_thread.is_alive():
            self._ai_loop_thread.join(timeout=2.0)

        try:
            self.runtime.shutdown()
        except Exception:
            pass


# ------------------------------------------------------------------------- #
#  ARGPARSE / MAIN
# ------------------------------------------------------------------------- #

def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="sirius",
        description="SIRIUS LOCAL AI ALFA – v2.0.0 runtime entrypoint",
    )

    parser.add_argument(
        "--no-ai-loop",
        action="store_true",
        help="Disable autonomous AI loop (runtime runs only on user input).",
    )

    parser.add_argument(
        "--cli",
        action="store_true",
        help="Force CLI mode (no GUI/TRAY/VOICE front-end).",
    )

    # Hooky pre budúce moduly – zatiaľ len placeholdery
    parser.add_argument(
        "--gui",
        action="store_true",
        help="Start GUI front-end (when implemented).",
    )
    parser.add_argument(
        "--tray",
        action="store_true",
        help="Start system tray front-end (when implemented).",
    )
    parser.add_argument(
        "--voice",
        action="store_true",
        help="Start voice front-end (when implemented).",
    )

    return parser.parse_args(argv)


def main(argv: Optional[list[str]] = None) -> None:
    if argv is None:
        argv = sys.argv[1:]

    args = parse_args(argv)

    app = SiriusApp(enable_ai_loop=not args.no_ai_loop)

    try:
        app.bootstrap()

        # Zatiaľ máme len CLI – GUI/TRAY/VOICE prídu neskôr
        # Logika:
        # – ak je --cli → spusti CLI
        # – ak neskôr pribudne GUI/TRAY/VOICE, tu sa rozhodne podľa args
        app.run_cli()

    finally:
        app.shutdown()


if __name__ == "__main__":
    main()
