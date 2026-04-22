from .base_command import BaseCommand
from .help_command import HelpCommand
from .run_command import RunCommand
from .system_info_command import SystemInfoCommand
from context.context_info_command import ContextInfoCommand


class CommandRegistry:
    """
    Centrálna registrácia príkazov pre SIRIUS LOCAL AI ALFA.
    """

    def __init__(self, context):
        self._commands: dict[str, BaseCommand] = {}
        self.context = context

    def register(self, command: BaseCommand):
        """
        Zaregistruje príkaz podľa jeho mena.
        """
        self._commands[command.name] = command

    def get(self, name: str) -> BaseCommand | None:
        """
        Vráti príkaz podľa mena alebo None.
        """
        return self._commands.get(name)

    def all(self) -> dict[str, BaseCommand]:
        """
        Vráti všetky registrované príkazy.
        """
        return self._commands


def create_default_registry(context) -> CommandRegistry:
    """
    Vytvorí predvolený register so základnými príkazmi.
    """
    registry = CommandRegistry(context)

    # HelpCommand potrebuje zoznam príkazov
    help_cmd = HelpCommand(registry._commands)

    registry.register(help_cmd)
    registry.register(RunCommand())
    registry.register(SystemInfoCommand())
    registry.register(ContextInfoCommand(context))

    return registry
