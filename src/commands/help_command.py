from .base_command import BaseCommand


class HelpCommand(BaseCommand):
    """
    Príkaz, ktorý vypíše zoznam dostupných príkazov v systéme.
    Podporuje aj detailný výpis pre konkrétny command.
    """

    name = "help"
    description = "Zobrazí zoznam dostupných príkazov alebo detail príkazu."

    def __init__(self, registry: dict[str, BaseCommand]):
        """
        registry = slovník {nazov_prikazu: CommandClass()}
        """
        self.registry = registry

    def execute(self, *args, **kwargs) -> str:
        """
        Ak je zadaný názov commandu, vypíše detail.
        Inak vypíše zoznam všetkých commandov.
        """
        # DETAILNÝ HELP: help <command>
        if args:
            command_name = args[0]
            command_obj = self.registry.get(command_name)

            if command_obj is None:
                return f"Neznámy príkaz: {command_name}"

            output = []
            output.append(f"=== Detail príkazu: {command_name} ===\n")

            # Popis
            desc = getattr(command_obj, "description", "Bez popisu")
            output.append(f"Popis:\n  {desc}\n")

            # Parametre
            params = command_obj.__class__.get_parameters()
            if params:
                output.append("Parametre:")
                for name, annotation in params:
                    output.append(f"  {name}: {annotation}")
            else:
                output.append("Parametre: (žiadne)")

            return "\n".join(output)

        # ZÁKLADNÝ HELP: help
        output_lines = []
        output_lines.append("=== Dostupné príkazy ===\n")

        for command_name, command_obj in sorted(self.registry.items()):
            desc = getattr(command_obj, "description", "Bez popisu")
            output_lines.append(f"- {command_name:<20} {desc}")

        output_lines.append("\nDetail príkazu:")
        output_lines.append("  python sirius.py help <command>")

        return "\n".join(output_lines)
