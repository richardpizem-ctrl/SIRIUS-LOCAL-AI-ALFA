from commands.base_command import BaseCommand
from context.context_manager import ContextManager


class TranslateCommand(BaseCommand):
    """
    Preloží text pomocou placeholder prekladača v ContextManageri.
    Použitie:
      translate en Ahoj svet
    """

    name = "translate"
    description = "Preloží text do cieľového jazyka (s validáciou, snapshotom a stavovým logom)."

    def __init__(self, context: ContextManager):
        self.context = context

    def execute(self, target_lang: str = None, *text):
        # -----------------------------
        #  VALIDÁCIA VSTUPU
        # -----------------------------
        if target_lang is None or not text:
            return "Použitie: translate <lang> <text>"

        # -----------------------------
        #  VALIDÁCIA KONTEXTU
        # -----------------------------
        if not self.context.validate():
            return "Chyba: Kontext nie je v konzistentnom stave."

        # -----------------------------
        #  SNAPSHOT PRED OPERÁCIOU
        # -----------------------------
        self.context.snapshot()

        # -----------------------------
        #  PRÍPRAVA TEXTU
        # -----------------------------
        sentence = " ".join(text)

        # -----------------------------
        #  PREKLAD
        # -----------------------------
        translated = self.context.translate(sentence, target_lang)

        # -----------------------------
        #  LOGOVANIE DO STAVU
        # -----------------------------
        # Uloží posledný preklad do state, aby ho mohli čítať iné moduly
        self.context.set_state("last_translation", translated)
        self.context.set_state("last_translation_lang", target_lang)

        # -----------------------------
        #  POTVRDENIE
        # -----------------------------
        return translated
