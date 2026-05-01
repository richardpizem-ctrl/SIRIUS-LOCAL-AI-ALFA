from .base_command import BaseCommand


class TriageTestCommand(BaseCommand):
    """
    Testovací príkaz pre AITE (Automatic Input Triage Engine).
    Umožňuje otestovať rozpoznanie typu vstupu a cieľovej cesty.
    """

    name = "triage-test"
    description = "Otestuje AITE triage na zadanom súbore."

    def __init__(self, runtime):
        self.runtime = runtime

    def execute(self, *args, **kwargs):
        if not args:
            return "Použi: triage-test <cesta>"

        path = args[0]

        try:
            result = self.runtime.aite.process(path)
        except Exception as e:
            return f"Chyba AITE: {e}"

        return result
