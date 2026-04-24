from commands.base_command import BaseCommand
from context.profile_manager import ProfileManager
from context.context_manager import ContextManager


class ContextProfileCommand(BaseCommand):
    """
    Správa profilov kontextu.
    Použitie:
      context-profile save <name>
      context-profile load <name>
      context-profile delete <name>
      context-profile list
      context-profile info <name>
    """

    name = "context-profile"
    description = "Spravuje profily kontextu (save/load/list/delete/info)."

    def __init__(self, context: ContextManager):
        self.context = context
        self.profiles = ProfileManager(context)

    def execute(self, action: str = None, name: str = None, *args):
        # -----------------------------
        #  VALIDÁCIA AKCIE
        # -----------------------------
        if action is None:
            return (
                "Použitie:\n"
                "  context-profile save <name>\n"
                "  context-profile load <name>\n"
                "  context-profile delete <name>\n"
                "  context-profile list\n"
                "  context-profile info <name>"
            )

        action = action.lower()

        # ============================================================
        #  SAVE
        # ============================================================
        if action == "save":
            if not name:
                return "Chyba: zadaj názov profilu. Použitie: context-profile save <name>"

            self.profiles.save_profile(name)
            return f"Profil '{name}' bol uložený."

        # ============================================================
        #  LOAD
        # ============================================================
        if action == "load":
            if not name:
                return "Chyba: zadaj názov profilu. Použitie: context-profile load <name>"

            result = self.profiles.load_profile(name)
            if not result:
                return f"Chyba: profil '{name}' neexistuje."

            return f"Profil '{name}' bol načítaný."

        # ============================================================
        #  DELETE
        # ============================================================
        if action == "delete":
            if not name:
                return "Chyba: zadaj názov profilu. Použitie: context-profile delete <name>"

            result = self.profiles.delete_profile(name)
            if not result:
                return f"Chyba: profil '{name}' neexistuje."

            return f"Profil '{name}' bol odstránený."

        # ============================================================
        #  LIST
        # ============================================================
        if action == "list":
            profiles = self.profiles.list_profiles()
            if not profiles:
                return "Žiadne profily neexistujú."

            out = ["Dostupné profily:"]
            for p in profiles:
                out.append(f"  - {p}")
            return "\n".join(out)

        # ============================================================
        #  INFO
        # ============================================================
        if action == "info":
            if not name:
                return "Chyba: zadaj názov profilu. Použitie: context-profile info <name>"

            info = self.profiles.get_profile_info(name)
            if not info:
                return f"Chyba: profil '{name}' neexistuje."

            return (
                f"Info o profile '{name}':\n"
                f"  - session položiek: {info['session_items']}\n"
                f"  - persistent položiek: {info['persistent_items']}\n"
                f"  - state položiek: {info['state_items']}\n"
                f"  - snapshotov v histórii: {info['history_snapshots']}"
            )

        # ============================================================
        #  NEZNÁMA AKCIA
        # ============================================================
        return f"Neznáma akcia '{action}'. Použi save/load/delete/list/info."
