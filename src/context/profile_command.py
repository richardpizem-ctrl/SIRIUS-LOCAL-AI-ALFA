from commands.base_command import BaseCommand
from context.profile_manager import ProfileManager
from context.context_manager import ContextManager


class ContextProfileCommand(BaseCommand):
    """
    Správa profilov kontextu.
    """

    name = "context-profile"
    description = "Spravuje profily kontextu (save/load/list/delete/info)."

    def __init__(self, context: ContextManager):
        self.context = context

    def execute(self, *args, **kwargs):
        # -----------------------------
        #  VALIDÁCIA VSTUPU
        # -----------------------------
        if not args:
            return (
                "Použitie:\n"
                "  context-profile save <name>\n"
                "  context-profile load <name>\n"
                "  context-profile delete <name>\n"
                "  context-profile list\n"
                "  context-profile info <name>"
            )

        action = args[0].lower()
        name = args[1] if len(args) > 1 else None

        # -----------------------------
        #  VALIDÁCIA KONTEXTU
        # -----------------------------
        if hasattr(self.context, "validate") and not self.context.validate():
            return "Chyba: Kontext nie je v konzistentnom stave."

        # Dynamické vytvorenie managera
        profiles = ProfileManager(self.context)

        # ============================================================
        #  SAVE
        # ============================================================
        if action == "save":
            if not name:
                return "Chyba: zadaj názov profilu. Použitie: context-profile save <name>"

            self.context.snapshot()
            profiles.save_profile(name)
            return f"Profil '{name}' bol uložený."

        # ============================================================
        #  LOAD
        # ============================================================
        if action == "load":
            if not name:
                return "Chyba: zadaj názov profilu. Použitie: context-profile load <name>"

            self.context.snapshot()
            result = profiles.load_profile(name)
            if not result:
                return f"Chyba: profil '{name}' neexistuje."

            return f"Profil '{name}' bol načítaný."

        # ============================================================
        #  DELETE
        # ============================================================
        if action == "delete":
            if not name:
                return "Chyba: zadaj názov profilu. Použitie: context-profile delete <name>"

            result = profiles.delete_profile(name)
            if not result:
                return f"Chyba: profil '{name}' neexistuje."

            return f"Profil '{name}' bol odstránený."

        # ============================================================
        #  LIST
        # ============================================================
        if action == "list":
            items = profiles.list_profiles()
            if not items:
                return "Žiadne profily neexistujú."

            out = ["Dostupné profily:"]
            for p in items:
                out.append(f"  - {p}")
            return "\n".join(out)

        # ============================================================
        #  INFO
        # ============================================================
        if action == "info":
            if not name:
                return "Chyba: zadaj názov profilu. Použitie: context-profile info <name>"

            info = profiles.get_profile_info(name)
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
