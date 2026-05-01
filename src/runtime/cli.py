import sys
from commands.registry import CommandRegistry
from commands.help_command import HelpCommand
from workflow.logger import WorkflowLogger


class CLI:
    """
    CLI pre SIRIUS LOCAL AI 2.0
    """

    def __init__(self, context):
        self.context = context
        self.logger = WorkflowLogger()

    def run(self, argv: list[str]):
        if len(argv) < 2:
            print("Usage: python sirius.py <command> [args...]")
            return

        command_name = argv[1]
        args = argv[2:]

        self.logger.info(f"CLI – received command: {command_name}")

        # HELP
        if command_name == "help":
            registry = CommandRegistry._commands
            help_cmd = HelpCommand(registry, self.context)

            if args:
                print(help_cmd.execute(args[0]))
            else:
                print(help_cmd.execute())
            return

        # FIND COMMAND
        command_class = CommandRegistry.get(command_name)

        if command_class is None:
            self.logger.error(f"Unknown command: {command_name}")
            print(f"Unknown command: {command_name}")
            return

        # CREATE INSTANCE
        try:
            command_instance = command_class(self.context)
        except Exception as exc:
            self.logger.error(f"Failed to create command instance: {exc}")
            print("Internal error.")
            return

        # VALIDATE
        if hasattr(command_instance, "validate") and not command_instance.validate():
            self.logger.error(f"Validation failed for: {command_name}")
            print("Validation failed.")
            return

        # EXECUTE
        try:
            result = command_instance.execute(*args)
            if result:
                print(result)
        except Exception as exc:
            self.logger.error(f"Execution error: {exc}")
            print("Execution failed.")
            return

        self.logger.info(f"Command finished: {command_name}")
