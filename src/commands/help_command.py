from .base_command import BaseCommand


class HelpCommand(BaseCommand):
    """
    Príkaz, ktorý vypíše zoznam dostupných príkazov v systéme.
    """

    name = "help"
    description = "Zobrazí zoznam dostupných príkazov."

    def __init__(self, registry: dict[str, BaseCommand]):
        """
        registry = slovník {nazov_prikazu: CommandClass()}
        """
        self.registry = registry

    def execute(self, *args, **kwargs):
        """
        Vypíše všetky príkazy a ich popisy.
        """
        output_lines = ["Dostupné príkazy:\n"]

        for command_name, command_obj in self.registry.items():
            output_lines.append(f"- {command_name}: {command_obj.description}")

        return "\n".join(output_lines)

