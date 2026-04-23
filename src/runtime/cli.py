import sys
from commands.registry import CommandRegistry
from commands.help_command import HelpCommand
from workflow.logger import WorkflowLogger


class CLI:
    """
    Jednoduchý CLI parser pre SIRIUS LOCAL AI.
    Umožňuje spúšťať commandy cez terminál:

        python sirius.py move_text_files "C:/src" "C:/target"
    """

    def __init__(self):
        self.logger = WorkflowLogger()

    def run(self, argv: list[str]):
        """
        Spracuje argumenty a spustí command.
        """
        if len(argv) < 2:
            print("Usage: python sirius.py <command> [args...]")
            return

        command_name = argv[1]
        args = argv[2:]

        self.logger.info(f"CLI – received command: {command_name}")

        # Špeciálny prípad: help (podpora aj pre help <command>)
        if command_name == "help":
            registry = CommandRegistry._commands
            help_cmd = HelpCommand(registry)

            if args:
                print(help_cmd.execute(args[0]))
            else:
                print(help_cmd.execute())

            return

        # Nájdeme command v registri
        command_class = CommandRegistry.get(command_name)

        if command_class is None:
            self.logger.error(f"Unknown command: {command_name}")
            print(f"Unknown command: {command_name}")
            return

        # Vytvoríme inštanciu commandu
        try:
            command_instance = command_class(*args)
        except TypeError:
            self.logger.error(f"Invalid arguments for command: {command_name}")
            print(f"Invalid arguments for command: {command_name}")
            return

        # Validácia
        if not command_instance.validate():
            self.logger.error(f"Validation failed for: {command_name}")
            print("Validation failed.")
            return

        # Spustenie
        self.logger.info(f"Executing command: {command_name}")
        command_instance.execute()
        self.logger.info(f"Command finished: {command_name}")
