from commands.base_command import BaseCommand
from context.context_manager import ContextManager


class TranslateCommand(BaseCommand):
    """
    Preloží text pomocou placeholder prekladača v ContextManageri.
    Použitie:
      translate <lang> <text>
    """

    name = "translate"
    description = "Preloží text do cieľového jazyka (s validáciou, snapshotom a stavovým logom)."

    def __init__(self, context: ContextManager):
        self.context = context

    def execute(self, *args, **kwargs):
        # -----------------------------
        #  VALIDÁCIA VSTUPU
        # -----------------------------
        if len(args) < 2:
            return "Použitie: translate <lang> <text>"

        target_lang = args[0]
        sentence = " ".join(args[1:])

        # -----------------------------
        #  VALIDÁCIA KONTEXTU
        # -----------------------------
        if hasattr(self.context, "validate") and not self.context.validate():
            return "Chyba: Kontext nie je v konzistentnom stave."

        # -----------------------------
        #  SNAPSHOT PRED OPERÁCIOU
        # -----------------------------
        if hasattr(self.context, "snapshot"):
            self.context.snapshot()

        # -----------------------------
        #  PREKLAD
        # -----------------------------
        translated = self.context.translate(sentence, target_lang)

        # -----------------------------
        #  LOGOVANIE DO STAVU (bezpečný merge)
        # -----------------------------
        self.context.merge({
            "last_translation": translated,
            "last_translation_lang": target_lang,
            "last_translation_source": sentence
        })

        # -----------------------------
        #  POTVRDENIE
        # -----------------------------
        return translated
