import inspect
from .base_command import BaseCommand


class HelpCommand(BaseCommand):
    """
    HelpCommand 4.0
    Poskytuje detailnú introspekciu príkazov pre CLI, NL Router a GUI.
    """

    name = "help"
    description = "Zobrazí zoznam príkazov alebo detailné informácie o konkrétnom príkaze."
    category = "system"

    required_identity = "FAMILY"   # Help je bezpečný pre všetkých
    risk_level = 0.0

    keywords = ["help", "commands", "info"]
    examples = ["help", "help move_files"]

    def __init__(self, command_registry):
        """
        command_registry: dict {command_name: CommandClass}
        """
        self.command_registry = command_registry

    # ---------------------------------------------------------
    # EXECUTION
    # ---------------------------------------------------------
    def execute(self, command_name: str = None):
        if not command_name:
            return self._list_commands()

        return self._describe_command(command_name)

    # ---------------------------------------------------------
    # LIST ALL COMMANDS
    # ---------------------------------------------------------
    def _list_commands(self):
        output = []
        for name, cmd in self.command_registry.items():
            output.append({
                "name": name,
                "description": cmd.description,
                "category": cmd.category,
                "required_identity": cmd.required_identity,
                "risk_level": cmd.risk_level
            })
        return output

    # ---------------------------------------------------------
    # DESCRIBE SINGLE COMMAND
    # ---------------------------------------------------------
    def _describe_command(self, name):
        cmd = self.command_registry.get(name)

        if not cmd:
            return {"error": f"Command '{name}' not found."}

        return {
            "name": cmd.name,
            "description": cmd.description,
            "category": cmd.category,
            "required_identity": cmd.required_identity,
            "risk_level": cmd.risk_level,
            "capabilities": cmd.capabilities,
            "keywords": cmd.keywords,
            "examples": cmd.examples,
            "parameters": cmd.get_parameters()
        }
