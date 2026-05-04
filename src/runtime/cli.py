import sys
import json
from commands.registry import CommandRegistry
from commands.help_command import HelpCommand
from workflow.logger import WorkflowLogger


class CLI:
    """
    CLI for SIRIUS LOCAL AI 4.0
    - OWNER identity enforcement
    - Security Family integration
    - Pretty JSON output
    - Command metadata support
    - Dependency injection for managers
    """

    def __init__(self, context, managers: dict):
        """
        managers = {
            "email": EmailManager(),
            "fs": FSAgent(),
            "workflow": WorkflowManager(),
            ...
        }
        """
        self.context = context
        self.managers = managers
        self.logger = WorkflowLogger()

    # --------------------------------------------------------
    # SAFE PRINT
    # --------------------------------------------------------
    @staticmethod
    def _print_json(data):
        print(json.dumps(data, indent=2, ensure_ascii=False))

    # --------------------------------------------------------
    # MAIN ENTRY
    # --------------------------------------------------------
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
            result = help_cmd.execute(args[0]) if args else help_cmd.execute()
            self._print_json(result)
            return

        # FIND COMMAND
        command_class = CommandRegistry.get(command_name)

        if command_class is None:
            self.logger.error(f"Unknown command: {command_name}")
            self._print_json({
                "status": "error",
                "message": f"Unknown command: {command_name}"
            })
            return

        # SECURITY FAMILY: IDENTITY CHECK
        required_identity = getattr(command_class, "required_identity", None)
        if required_identity and self.context.identity != required_identity:
            self._print_json({
                "status": "error",
                "message": f"Command '{command_name}' requires identity '{required_identity}'."
            })
            return

        # CREATE INSTANCE WITH DEPENDENCY INJECTION
        try:
            command_instance = command_class(self.context, **self.managers)
        except Exception as exc:
            self.logger.error(f"Failed to create command instance: {exc}")
            self._print_json({
                "status": "error",
                "message": "Internal error: failed to initialize command."
            })
            return

        # VALIDATE
        if hasattr(command_instance, "validate") and not command_instance.validate():
            self.logger.error(f"Validation failed for: {command_name}")
            self._print_json({
                "status": "error",
                "message": "Validation failed."
            })
            return

        # EXECUTE
        try:
            result = command_instance.execute(*args)
            if result is not None:
                self._print_json(result)

        except Exception as exc:
            self.logger.error(f"Execution error: {exc}")
            self._print_json({
                "status": "error",
                "message": "Execution failed.",
                "details": str(exc)
            })
            return

        self.logger.info(f"Command finished: {command_name}")
