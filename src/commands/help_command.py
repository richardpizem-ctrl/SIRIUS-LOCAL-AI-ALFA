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

    def execute(self, *args, **kwargs) -> str:
        """
        Vypíše všetky príkazy a ich popisy v peknom formáte.
        """
        output_lines = []
        output_lines.append("=== Dostupné príkazy ===\n")

        # Zoradíme príkazy podľa názvu
        for command_name, command_obj in sorted(self.registry.items()):
            desc = getattr(command_obj, "description", "Bez popisu")
            output_lines.append(f"- {command_name:<20} {desc}")

        output_lines.append("\nPoužitie:")
        output_lines.append("  python sirius.py <command> [args...]")

        return "\n".join(output_lines)
