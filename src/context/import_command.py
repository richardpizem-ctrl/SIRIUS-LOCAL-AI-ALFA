from commands.base_command import BaseCommand
from context.context_manager import ContextManager
import json
import os


class ContextImportCommand(BaseCommand):
    """
    Importuje kontext zo JSON súboru.
    Použitie:
      context-import all <filename>
      context-import session <filename>
      context-import persistent <filename>
      context-import state <filename>
      context-import history <filename>
    """

    name = "context-import"
    description = "Importuje kontext alebo jeho časti zo JSON súboru."

    def __init__(self, context: ContextManager):
        self.context = context

    def execute(self, section: str = None, filename: str = None, *args):
        # -----------------------------
        #  VALIDÁCIA VSTUPU
        # -----------------------------
        if section is None or filename is None:
            return (
                "Použitie:\n"
                "  context-import all <filename>\n"
                "  context-import session <filename>\n"
                "  context-import persistent <filename>\n"
                "  context-import state <filename>\n"
                "  context-import history <filename>"
            )

        section = section.lower()

        if not os.path.isfile(filename):
            return f"Chyba: súbor '{filename}' neexistuje."

        # -----------------------------
        #  NAČÍTANIE JSON
        # -----------------------------
        try:
            with open(filename, "r", encoding="utf-8") as f:
                data = json.load(f)
        except Exception as e:
            return f"Chyba pri načítaní JSON: {e}"

        # -----------------------------
        #  IMPORT PODĽA SEKCIÍ
        # -----------------------------
        if section == "all":
            if not isinstance(data, dict):
                return "Chyba: JSON musí obsahovať objekt s kľúčmi session/persistent/state/history."

            self.context.session_memory = data.get("session", [])
            self.context.persistent_memory = data.get("persistent", {})
            self.context.state = data.get("state", {})
            self.context.history = data.get("history", [])

        elif section == "session":
            if not isinstance(data, list):
                return "Chyba: session musí byť zoznam."
            self.context.session_memory = data

        elif section == "persistent":
            if not isinstance(data, dict):
                return "Chyba: persistent musí byť objekt."
            self.context.persistent_memory = data

        elif section == "state":
            if not isinstance(data, dict):
                return "Chyba: state musí byť objekt."
            self.context.state = data

        elif section == "history":
            if not isinstance(data, list):
                return "Chyba: history musí byť zoznam snapshotov."
            self.context.history = data

        else:
            return f"Neznáma sekcia '{section}'. Použi: all/session/persistent/state/history."

        # -----------------------------
        #  VALIDÁCIA KONTEXTU PO IMPORTe
        # -----------------------------
        if not self.context.validate():
            return "Upozornenie: import prebehol, ale kontext nie je v konzistentnom stave."

        # -----------------------------
        #  POTVRDENIE
        # -----------------------------
        return f"Kontextová sekcia '{section}' bola importovaná zo súboru '{filename}'."
