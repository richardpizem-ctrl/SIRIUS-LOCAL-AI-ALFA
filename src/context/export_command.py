from commands.base_command import BaseCommand
from context.context_manager import ContextManager
import json
import os


class ContextExportCommand(BaseCommand):
    """
    Exportuje kontext do JSON súboru.
    Použitie:
      context-export all <filename>
      context-export session <filename>
      context-export persistent <filename>
      context-export state <filename>
      context-export history <filename>
    """

    name = "context-export"
    description = "Exportuje kontext alebo jeho časti do JSON súboru."

    def __init__(self, context: ContextManager):
        self.context = context

    def execute(self, section: str = None, filename: str = None, *args):
        # -----------------------------
        #  VALIDÁCIA VSTUPU
        # -----------------------------
        if section is None or filename is None:
            return (
                "Použitie:\n"
                "  context-export all <filename>\n"
                "  context-export session <filename>\n"
                "  context-export persistent <filename>\n"
                "  context-export state <filename>\n"
                "  context-export history <filename>"
            )

        section = section.lower()

        # -----------------------------
        #  PRÍPRAVA DÁT NA EXPORT
        # -----------------------------
        if section == "all":
            data = {
                "session": self.context.session_memory,
                "persistent": self.context.persistent_memory,
                "state": self.context.state,
                "history": self.context.history,
            }

        elif section == "session":
            data = self.context.session_memory

        elif section == "persistent":
            data = self.context.persistent_memory

        elif section == "state":
            data = self.context.state

        elif section == "history":
            data = self.context.history

        else:
            return f"Neznáma sekcia '{section}'. Použi: all/session/persistent/state/history."

        # -----------------------------
        #  EXPORT DO JSON
        # -----------------------------
        try:
            with open(filename, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
        except Exception as e:
            return f"Chyba pri exporte: {e}"

        # -----------------------------
        #  POTVRDENIE
        # -----------------------------
        return f"Kontextová sekcia '{section}' bola exportovaná do súboru '{filename}'."
