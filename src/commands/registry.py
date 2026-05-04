from .base_command import BaseCommand
from .help_command import HelpCommand
from .run_command import RunCommand
from .system_info_command import SystemInfoCommand

from context.context_info_command import ContextInfoCommand
from context.context_set_command import ContextSetCommand
from context.context_clear_command import ContextClearCommand
from context.memory_save_command import MemorySaveCommand
from context.memory_load_command import MemoryLoadCommand
from context.context_dump_command import ContextDumpCommand
from context.translate_command import TranslateCommand

from commands.triage_test_command import TriageTestCommand
from commands.move_text_files import MoveTextFilesCommand


class CommandRegistry:
    """
    Command Registry 4.0
    Centrálna registrácia príkazov pre SIRIUS LOCAL AI 4.0.

    Novinky vo verzii 4.0:
    - registruje command TRIEDY, nie inštancie
    - podporuje introspekciu 4.0
    - poskytuje metadata pre NL Router 4.0
    - podporuje dynamickú inštanciáciu cez Runtime Core 4.0
    - podporuje SECURITY FAMILY 4.0 (identity, risk, capabilities)
    """

    def __init__(self, context):
        self._commands: dict[str, type[BaseCommand]] = {}
        self.context = context

    # ---------------------------------------------------------
    # REGISTRATION
    # ---------------------------------------------------------
    def register(self, command_cls: type[BaseCommand]):
        """
        Zaregistruje command TRIEDU podľa jej mena.
        """
        if not issubclass(command_cls, BaseCommand):
            raise TypeError(f"Command {command_cls} must inherit from BaseCommand.")

        self._commands[command_cls.name] = command_cls

    # ---------------------------------------------------------
    # LOOKUP
    # ---------------------------------------------------------
    def get(self, name: str) -> type[BaseCommand] | None:
        """
        Vráti command TRIEDU podľa mena.
        """
        return self._commands.get(name)

    def all(self) -> dict[str, type[BaseCommand]]:
        """
        Vráti všetky registrované command triedy.
        """
        return self._commands

    # ---------------------------------------------------------
    # DYNAMIC INSTANTIATION (v4.0)
    # ---------------------------------------------------------
    def create_instance(self, name: str, *args, **kwargs) -> BaseCommand | None:
        """
        Vytvorí inštanciu commandu podľa mena.
        Runtime Core 4.0 bude používať iba toto.
        """
        cmd_cls = self.get(name)
        if not cmd_cls:
            return None

        return cmd_cls(*args, **kwargs)


# ---------------------------------------------------------
# DEFAULT REGISTRY (v4.0)
# ---------------------------------------------------------
def create_default_registry(context) -> CommandRegistry:
    """
    Vytvorí predvolený register so základnými príkazmi.
    Registrujú sa TRIEDY, nie inštancie.
    """
    registry = CommandRegistry(context)

    # HelpCommand potrebuje registry, ale registrujeme TRIEDU
    registry.register(HelpCommand)
    registry.register(RunCommand)
    registry.register(SystemInfoCommand)

    # Kontextové príkazy
    registry.register(ContextInfoCommand)
    registry.register(ContextSetCommand)
    registry.register(ContextClearCommand)
    registry.register(MemorySaveCommand)
    registry.register(MemoryLoadCommand)
    registry.register(ContextDumpCommand)
    registry.register(TranslateCommand)

    # AITE testovací príkaz
    registry.register(TriageTestCommand)

    # MoveTextFilesCommand (FS-AGENT)
    registry.register(MoveTextFilesCommand)

    return registry
