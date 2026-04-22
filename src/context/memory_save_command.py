from commands.base_command import BaseCommand
from context.context_manager import ContextManager


class MemorySaveCommand(BaseCommand):
    """
    Uloží hodnotu do dlhodobej pamäte.
    Použitie:
      memory-save language english
    """

    name = "memory-save"
    description = "Uloží hodnotu do dlhodobej pamäte AI."

    def __init__(self, context: ContextManager):
        self.context = context

    def execute(self, key: str = None, value: str = None, *args):
        if key is None or value is None:
            return "Použitie: memory-save <key> <value>"

        self.context.store(key, value)
        return f"Uložené do pamäte: {key} = {value}"
