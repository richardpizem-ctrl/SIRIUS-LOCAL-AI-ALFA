from commands.base_command import BaseCommand
from context.context_manager import ContextManager


class TranslateCommand(BaseCommand):
    """
    TranslateCommand 4.0
    Translates text using the placeholder translator in ContextManager.

    New in v4.0:
    - NL Router metadata
    - SECURITY FAMILY enforcement
    - risk-aware execution
    - capability flags (context_read, context_write)
    - snapshot before translation
    - structured output for Workflow Engine 4.0
    - safe merge of translation metadata into state
    """

    # ---------------------------------------------------------
    # METADATA (v4.0)
    # ---------------------------------------------------------
    name = "translate"
    description = "Translates text into a target language with validation, snapshot, and state logging."
    category = "language"

    required_identity = "OWNER"     # Only OWNER can run translation commands
    risk_level = 0.3                # Low-medium risk (state modification)
    capabilities = ["context_read", "context_write"]

    keywords = ["translate", "language", "text"]
    examples = ["translate en Hello world"]

    # ---------------------------------------------------------
    # INIT
    # ---------------------------------------------------------
    def __init__(self, context: ContextManager):
        self.context = context

    # ---------------------------------------------------------
    # EXECUTION (v4.0)
    # ---------------------------------------------------------
    def execute(self, *args, **kwargs):
        """
        Translates text using the context's translation engine.
        """

        # -----------------------------
        # INPUT VALIDATION
        # -----------------------------
        if len(args) < 2:
            return {
                "status": "error",
                "message": "Usage: translate <lang> <text>"
            }

        target_lang = args[0]
        sentence = " ".join(args[1:])

        # -----------------------------
        # CONTEXT VALIDATION
        # -----------------------------
        if hasattr(self.context, "validate") and not self.context.validate():
            return {
                "status": "invalid",
                "message": "Context is not in a consistent state."
            }

        # -----------------------------
        # SNAPSHOT BEFORE TRANSLATION
        # -----------------------------
        if hasattr(self.context, "snapshot"):
            self.context.snapshot()

        # -----------------------------
        # PERFORM TRANSLATION
        # -----------------------------
        translated = self.context.translate(sentence, target_lang)

        # -----------------------------
        # LOG TRANSLATION INTO STATE
        # -----------------------------
        self.context.merge({
            "last_translation": translated,
            "last_translation_lang": target_lang,
            "last_translation_source": sentence
        })

        # -----------------------------
        # SUCCESS RESPONSE
        # -----------------------------
        return {
            "status": "success",
            "source_text": sentence,
            "target_lang": target_lang,
            "translated_text": translated,
            "message": "Translation completed successfully."
        }
