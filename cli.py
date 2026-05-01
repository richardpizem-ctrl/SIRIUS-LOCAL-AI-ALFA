import sys
from runtime.runtime_manager import RuntimeManager


class SiriusCLI:
    """
    Jednoduché CLI rozhranie pre SIRIUS-LOCAL-AI
    - podporuje NL príkazy
    - podporuje AI tasky
    - slúži ako terminálový vstup pre runtime
    """

    def __init__(self):
        self.rm = RuntimeManager()
        self.rm.initialize()

    # --------------------------------------------------------
    # HLAVNÝ VSTUP
    # --------------------------------------------------------
    def run(self, argv):
        if len(argv) < 2:
            self._print_help()
            return

        command = argv[1].lower()

        # ----------------------------------------------------
        # PRIRODZENÝ JAZYK
        # sirius nl "daj vs code doprava"
        # ----------------------------------------------------
        if command == "nl":
            text = " ".join(argv[2:])
            result = self.rm.handle_nl(text)
            self._print_result(result)
            return

        # ----------------------------------------------------
        # PRIAME AI TASKY
        # sirius task snap_right app="vs code"
        # ----------------------------------------------------
        if command == "task":
            if len(argv) < 3:
                print("Chýba názov tasku.")
                return

            goal = argv[2]
            args = self._parse_args(argv[3:])
            result = self.rm.handle_ai_task(goal, args)
            self._print_result(result)
            return

        # ----------------------------------------------------
        # SYSTÉMOVÝ KONTEXT
        # sirius context
        # ----------------------------------------------------
        if command == "context":
            result = self.rm.get_ai_context()
            self._print_result(result)
            return

        # ----------------------------------------------------
        # HELP
        # ----------------------------------------------------
        if command == "help":
            self._print_help()
            return

        print(f"Neznámy príkaz: {command}")
        self._print_help()

    # --------------------------------------------------------
    # POMOCNÉ FUNKCIE
    # --------------------------------------------------------

    def _parse_args(self, items):
        """
        Prevedie argumenty vo forme key=value na dict.
        """
        args = {}
        for item in items:
            if "=" in item:
                key, value = item.split("=", 1)
                args[key] = value
        return args

    def _print_result(self, result):
        """
        Jednotné formátovanie výstupu.
        """
        print("--------------------------------------------------")
        for k, v in result.items():
            print(f"{k}: {v}")
        print("--------------------------------------------------")

    def _print_help(self):
        print("""
SIRIUS CLI – dostupné príkazy:

  sirius nl "<prirodzená veta>"
      - spracuje prirodzený jazyk cez NL Router
      - napr. sirius nl "daj vs code doprava"

  sirius task <goal> key=value key=value
      - priame volanie autonómneho runtime agenta
      - napr. sirius task move_file source=a.txt target=data/

  sirius context
      - vráti systémový kontext

  sirius help
      - zobrazí túto nápovedu
""")



# ------------------------------------------------------------
# SPÚŠŤACÍ BOD
# ------------------------------------------------------------

if __name__ == "__main__":
    cli = SiriusCLI()
    cli.run(sys.argv)
