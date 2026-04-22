from .base_command import BaseCommand
from .help_command import HelpCommand
from .run_command import RunCommand
from .system_info_command import SystemInfoCommand


class CommandRegistry:
    """
    Centrálna registrácia príkazov pre SIRIUS LOCAL AI ALFA.
    Umožňuje:
    - registrovať príkazy
    - získavať príkazy podľa mena
    - vypísať všetky príkazy (pre help)
    """

    def __init__(self):
        self._commands: dict[str, BaseCommand] = {}

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


def create_default_registry() -> CommandRegistry:
    """
    Vytvorí predvolený register so základnými príkazmi.
    """
    registry = CommandRegistry()

    # Najprv vytvoríme prázdny registry, aby sme ho mohli odovzdať HelpCommand
    help_cmd = HelpCommand(registry._commands)

    registry.register(help_cmd)
    registry.register(RunCommand())
    registry.register(SystemInfoCommand())

    return registry
