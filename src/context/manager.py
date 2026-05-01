class ContextManager:
    """
    Spravuje kontext SIRIUS LOCAL AI ALFA.
    """

    def __init__(self):
        self.session_memory: list[str] = []
        self.persistent_memory: dict[str, str] = {}
        self.state: dict[str, str] = {}

        self.history: list[dict] = []
        self.max_history = 20

    # ============================================================
    #  KRÁTKODOBÁ PAMÄŤ
    # ============================================================
    def remember(self, text: str):
        self.session_memory.append(text)

    def get_recent(self, limit: int = 5) -> list[str]:
        return self.session_memory[-limit:]

    # ============================================================
    #  DLHODOBÁ PAMÄŤ
    # ============================================================
    def store(self, key: str, value: str):
        self.persistent_memory[key] = value

    def recall(self, key: str) -> str | None:
        return self.persistent_memory.get(key)

    # ============================================================
    #  PREKLAD
    # ============================================================
    def translate(self, text: str, target_lang: str = "en") -> str:
        return f"[translate → {target_lang}] {text}"

    # ============================================================
    #  STAV
    # ============================================================
    def set_state(self, key: str, value: str):
        self.state[key] = value

    def get_state(self, key: str) -> str | None:
        return self.state.get(key)

    # ============================================================
    #  VALIDÁCIA
    # ============================================================
    def validate(self) -> bool:
        if not isinstance(self.session_memory, list):
            return False
        if not isinstance(self.persistent_memory, dict):
            return False
        if not isinstance(self.state, dict):
            return False
        if not isinstance(self.history, list):
            return False

        # Validácia snapshotov
        for snap in self.history:
            if not isinstance(snap, dict):
                return False
            if "session" not in snap or "persistent" not in snap or "state" not in snap:
                return False

        return True

    # ============================================================
    #  SNAPSHOT
    # ============================================================
    def snapshot(self):
        snap = {
            "session": list(self.session_memory),
            "persistent": dict(self.persistent_memory),
            "state": dict(self.state),
        }
        self.history.append(snap)

        if len(self.history) > self.max_history:
            self.history.pop(0)

    # ============================================================
    #  ROLLBACK
    # ============================================================
    def rollback(self, steps: int = 1):
        if steps <= 0 or steps > len(self.history):
            return False

        snap = self.history[-steps]

        self.session_memory = list(snap["session"])
        self.persistent_memory = dict(snap["persistent"])
        self.state = dict(snap["state"])

        # odstrániť snapshoty po rollbacku
        del self.history[-steps+1:]

        return True

    # ============================================================
    #  DIFF
    # ============================================================
    def diff(self, other_state: dict) -> dict:
        differences = {}

        # keys in other_state
        for key, value in other_state.items():
            if self.state.get(key) != value:
                differences[key] = {
                    "current": self.state.get(key),
                    "incoming": value
                }

        # keys missing in other_state
        for key in self.state:
            if key not in other_state:
                differences[key] = {
                    "current": self.state[key],
                    "incoming": None
                }

        return differences

    # ============================================================
    #  MERGE
    # ============================================================
    def merge(self, new_state: dict):
        for key, value in new_state.items():
            # bezpečný merge
            if isinstance(key, str):
                self.state[key] = value
