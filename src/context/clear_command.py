from commands.base_command import BaseCommand
from context.context_manager import ContextManager


class ContextClearCommand(BaseCommand):
    """
    Vymaže krátkodobú pamäť AI.
    """

    name = "context-clear"
    description = "Vymaže krátkodobú pamäť (session memory)."

    def __init__(self, context: ContextManager):
        self.context = context

    def execute(self, *args):
        self.context.session_memory.clear()
        return "Krátkodobá pamäť bola vymazaná."
