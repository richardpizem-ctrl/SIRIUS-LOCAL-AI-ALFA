from .base_command import BaseCommand


class RunCommand(BaseCommand):
    """
    Príkaz, ktorý spustí akciu alebo úlohu v systéme.
    """

    name = "run"
    description = "Spustí zadanú akciu alebo úlohu."

    def execute(self, *args, **kwargs):
        """
        Vykoná akciu podľa argumentov.
        Zatiaľ len demonštračná implementácia.
        """
        if not args:
            return "Nebola zadaná žiadna akcia na spustenie."

        action = args[0]
        return f"Spúšťam akciu: {action}"

