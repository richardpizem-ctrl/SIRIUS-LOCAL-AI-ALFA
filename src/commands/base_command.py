import inspect


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

    @classmethod
    def get_parameters(cls):
        """
        Vráti zoznam parametrov __init__ metódy pre introspekciu.
        Používa sa v HelpCommand a CLI.
        """
        signature = inspect.signature(cls.__init__)
        params = []

        for name, param in signature.parameters.items():
            if name == "self":
                continue
            params.append((name, str(param.annotation)))

        return params
