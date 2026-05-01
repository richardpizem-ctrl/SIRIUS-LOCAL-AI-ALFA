from commands.base_command import BaseCommand
from context.context_manager import ContextManager
import json
import os
import copy


class ContextMergeCommand(BaseCommand):
    name = "context-merge"
    description = "Zlúči externý JSON kontext s aktuálnym kontextom."

    def __init__(self, context: ContextManager):
        self.context = context

    def execute(self, *args, **kwargs):
        # -----------------------------
        #  VALIDÁCIA VSTUPU
        # -----------------------------
        if len(args) < 2:
            return (
                "Použitie:\n"
                "  context-merge all <filename>\n"
                "  context-merge session <filename>\n"
                "  context-merge persistent <filename>\n"
                "  context-merge state <filename>\n"
                "  context-merge history <filename>"
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
                incoming = json.load(f)
        except Exception as e:
            return f"Chyba pri načítaní JSON: {e}"

        # -----------------------------
        #  SNAPSHOT PRED MERGE
        # -----------------------------
        if hasattr(self.context, "snapshot"):
            self.context.snapshot()

        # -----------------------------
        #  MERGE PODĽA SEKCIÍ
        # -----------------------------
        try:
            if section == "all":
                if not isinstance(incoming, dict):
                    return "Chyba: JSON musí obsahovať objekt."

                # SESSION
                if isinstance(incoming.get("session"), list):
                    for item in incoming["session"]:
                        if isinstance(item, str):
                            self.context.session_memory.append(item)

                # PERSISTENT
                if isinstance(incoming.get("persistent"), dict):
                    for k, v in incoming["persistent"].items():
                        if isinstance(k, str) and isinstance(v, str):
                            self.context.persistent_memory[k] = v

                # STATE
                if isinstance(incoming.get("state"), dict):
                    for k, v in incoming["state"].items():
                        if isinstance(k, str) and isinstance(v, str):
                            self.context.state[k] = v

                # HISTORY
                if isinstance(incoming.get("history"), list):
                    for snap in incoming["history"]:
                        if isinstance(snap, dict):
                            self.context.history.append(copy.deepcopy(snap))

                    # rešpektovať max_history
                    self.context.history = self.context.history[-self.context.max_history:]

            elif section == "session":
                if not isinstance(incoming, list):
                    return "Chyba: session musí byť zoznam."
                for item in incoming:
                    if isinstance(item, str):
                        self.context.session_memory.append(item)

            elif section == "persistent":
                if not isinstance(incoming, dict):
                    return "Chyba: persistent musí byť objekt."
                for k, v in incoming.items():
                    if isinstance(k, str) and isinstance(v, str):
                        self.context.persistent_memory[k] = v

            elif section == "state":
                if not isinstance(incoming, dict):
                    return "Chyba: state musí byť objekt."
                for k, v in incoming.items():
                    if isinstance(k, str) and isinstance(v, str):
                        self.context.state[k] = v

            elif section == "history":
                if not isinstance(incoming, list):
                    return "Chyba: history musí byť zoznam snapshotov."
                for snap in incoming:
                    if isinstance(snap, dict):
                        self.context.history.append(copy.deepcopy(snap))
                self.context.history = self.context.history[-self.context.max_history:]

            else:
                return f"Neznáma sekcia '{section}'."

        except Exception as e:
            return f"Chyba pri merge: {e}"

        # -----------------------------
        #  VALIDÁCIA PO MERGE
        # -----------------------------
        if hasattr(self.context, "validate") and not self.context.validate():
            return "Upozornenie: merge prebehol, ale kontext nie je v konzistentnom stave."

        return f"Kontextová sekcia '{section}' bola zlúčená so súborom '{filename}'."
