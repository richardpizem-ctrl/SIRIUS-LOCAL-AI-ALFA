from commands.base_command import BaseCommand
from context.context_manager import ContextManager


class MemoryLoadCommand(BaseCommand):
    """
    Načíta hodnotu z dlhodobej pamäte.
    Použitie:
      memory-load language
    """

    name = "memory-load"
    description = "Načíta hodnotu z dlhodobej pamäte AI."

    def __init__(self, context: ContextManager):
        self.context = context

    def execute(self, key: str = None, *args):
        if key is None:
            return "Použitie: memory-load <key>"

        value = self.context.recall(key)
        if value is None:
            return f"V pamäti sa nenašlo: {key}"

        return f"{key} = {value}"
