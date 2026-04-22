class BaseCommand:
    """
    Základná trieda pre všetky príkazy v systéme SIRIUS LOCAL AI ALFA.
    Každý príkaz musí implementovať metódu `execute()`.
    """

    name: str = "base"
    description: str = "Base command class"

    def execute(self, *args, **kwargs):
        """
        Metóda, ktorú musia potomkovia prepísať.
        """
        raise NotImplementedError("Subclasses must implement execute().")

