from .base_command import BaseCommand

class TriageTestCommand(BaseCommand):
    name = "triage-test"

    def __init__(self, runtime):
        self.runtime = runtime

    def execute(self, args: list[str]):
        if not args:
            return "Použi: triage-test <cesta>"

        path = args[0]
        result = self.runtime.aite.process(path)
        return result
