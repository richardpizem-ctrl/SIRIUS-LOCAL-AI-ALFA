from commands.base_command import BaseCommand
from context.context_manager import ContextManager
import json
import os
import copy


class ContextImportCommand(BaseCommand):
    """
    Importuje kontext zo JSON súboru.
    """

    name = "context-import"
    description = "Importuje kontext alebo jeho časti zo JSON súboru."

    def __init__(self, context: ContextManager):
        self.context = context

    def execute(self, *args, **kwargs):
        # -----------------------------
        #  VALIDÁCIA VSTUPU
        # -----------------------------
        if len(args) < 2:
            return (
                "Použitie:\n"
                "  context-import all <filename>\n"
                "  context-import session <filename>\n"
                "  context-import persistent <filename>\n"
                "  context-import state <filename>\n"
                "  context-import history <filename>"
            )

        section = args[0].lower()
        filename = args[1]

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
        try:
            if section == "all":
                if not isinstance(data, dict):
                    return "Chyba: JSON musí obsahovať objekt s kľúčmi session/persistent/state/history."

                self.context.session_memory = copy.deepcopy(data.get("session", []))
                self.context.persistent_memory = copy.deepcopy(data.get("persistent", {}))
                self.context.state = copy.deepcopy(data.get("state", {}))

                history = data.get("history", [])
                if isinstance(history, list):
                    self.context.history = history[-self.context.max_history:]
                else:
                    return "Chyba: history musí byť zoznam snapshotov."

            elif section == "session":
                if not isinstance(data, list):
                    return "Chyba: session musí byť zoznam."
                self.context.session_memory = copy.deepcopy(data)

            elif section == "persistent":
                if not isinstance(data, dict):
                    return "Chyba: persistent musí byť objekt."
                self.context.persistent_memory = copy.deepcopy(data)

            elif section == "state":
                if not isinstance(data, dict):
                    return "Chyba: state musí byť objekt."
                self.context.state = copy.deepcopy(data)

            elif section == "history":
                if not isinstance(data, list):
                    return "Chyba: history musí byť zoznam snapshotov."
                self.context.history = data[-self.context.max_history:]

            else:
                return f"Neznáma sekcia '{section}'. Použi: all/session/persistent/state/history."

        except Exception as e:
            return f"Chyba pri importe: {e}"

        # -----------------------------
        #  VALIDÁCIA KONTEXTU PO IMPORTe
        # -----------------------------
        if hasattr(self.context, "validate") and not self.context.validate():
            return "Upozornenie: import prebehol, ale kontext nie je v konzistentnom stave."

        return f"Kontextová sekcia '{section}' bola importovaná zo súboru '{filename}'."
