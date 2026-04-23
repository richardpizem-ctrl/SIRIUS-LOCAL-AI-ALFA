from commands.base_command import BaseCommand
from context.context_manager import ContextManager


class TranslateCommand(BaseCommand):
    """
    Preloží text pomocou placeholder prekladača v ContextManageri.
    Použitie:
      translate en Ahoj svet
    """

    name = "translate"
    description = "Preloží text do cieľového jazyka."

    def __init__(self, context: ContextManager):
        self.context = context

    def execute(self, target_lang: str = None, *text):
        if target_lang is None or not text:
            return "Použitie: translate <lang> <text>"

        sentence = " ".join(text)
        return self.context.translate(sentence, target_lang)
