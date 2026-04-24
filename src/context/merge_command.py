from commands.base_command import BaseCommand
from context.context_manager import ContextManager
import json
import os


class ContextMergeCommand(BaseCommand):
    """
    Zlúči externý JSON kontext s aktuálnym kontextom.
    Použitie:
      context-merge all <filename>
      context-merge session <filename>
      context-merge persistent <filename>
      context-merge state <filename>
      context-merge history <filename>
    """

    name = "context-merge"
    description = "Zlúči externý JSON kontext s aktuálnym kontextom."

    def __init__(self, context: ContextManager):
        self.context = context

    def execute(self, section: str = None, filename: str = None, *args):
        # -----------------------------
        #  VALIDÁCIA VSTUPU
        # -----------------------------
        if section is None or filename is None:
            return (
                "Použitie:\n"
                "  context-merge all <filename>\n"
                "  context-merge session <filename>\n"
                "  context-merge persistent <filename>\n"
                "  context-merge state <filename>\n"
                "  context-merge history <filename>"
            )

        section = section.lower()

        if not os.path.isfile(filename):
            return f"Chyba: súbor '{filename}' neexistuje."

        # -----------------------------
        #  NAČÍTANIE JSON
        # -----------------------------
        try:
            with open(filename, "r", encoding="utf-8") as f:
                incoming = json.load(f)
        except Exception as e:
            return f"Chyba pri načítaní JSON: {e}"

        # -----------------------------
        #  MERGE PODĽA SEKCIÍ
        # -----------------------------
        if section == "all":
            if not isinstance(incoming, dict):
                return "Chyba: JSON musí obsahovať objekt s kľúčmi session/persistent/state/history."

            # SESSION: append
            if isinstance(incoming.get("session"), list):
                self.context.session_memory.extend(incoming["session"])

            # PERSISTENT: merge keys
            if isinstance(incoming.get("persistent"), dict):
                self.context.persistent_memory.update(incoming["persistent"])

            # STATE: merge keys
            if isinstance(incoming.get("state"), dict):
                self.context.state.update(incoming["state"])

            # HISTORY: append snapshots
            if isinstance(incoming.get("history"), list):
                self.context.history.extend(incoming["history"])

        elif section == "session":
            if not isinstance(incoming, list):
                return "Chyba: session musí byť zoznam."
            self.context.session_memory.extend(incoming)

        elif section == "persistent":
            if not isinstance(incoming, dict):
                return "Chyba: persistent musí byť objekt."
            self.context.persistent_memory.update(incoming)

        elif section == "state":
            if not isinstance(incoming, dict):
                return "Chyba: state musí byť objekt."
            self.context.state.update(incoming)

        elif section == "history":
            if not isinstance(incoming, list):
                return "Chyba: history musí byť zoznam snapshotov."
            self.context.history.extend(incoming)

        else:
            return f"Neznáma sekcia '{section}'. Použi: all/session/persistent/state/history."

        # -----------------------------
        #  VALIDÁCIA KONTEXTU PO MERGE
        # -----------------------------
        if not self.context.validate():
            return "Upozornenie: merge prebehol, ale kontext nie je v konzistentnom stave."

        # -----------------------------
        #  POTVRDENIE
        # -----------------------------
        return f"Kontextová sekcia '{section}' bola zlúčená so súborom '{filename}'."
