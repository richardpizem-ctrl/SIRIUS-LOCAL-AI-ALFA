class ContextManager:
    """
    Spravuje kontext SIRIUS LOCAL AI ALFA.

    Obsahuje:
    - krátkodobú pamäť (session memory)
    - dlhodobú pamäť (persistent memory)
    - prekladové funkcie (placeholder)
    - stav systému
    - história kontextu (snapshots)
    - validáciu kontextu
    - diff/merge mechanizmy
    """

    def __init__(self):
        # Primárne úložiská
        self.session_memory: list[str] = []
        self.persistent_memory: dict[str, str] = {}
        self.state: dict[str, str] = {}

        # História kontextu
        self.history: list[dict] = []
        self.max_history = 20  # limit pre rollback

    # ============================================================
    #  KRÁTKODOBÁ PAMÄŤ
    # ============================================================
    def remember(self, text: str):
        """Uloží text do krátkodobej pamäte."""
        self.session_memory.append(text)

    def get_recent(self, limit: int = 5) -> list[str]:
        """Vráti posledné položky z krátkodobej pamäte."""
        return self.session_memory[-limit:]

    # ============================================================
    #  DLHODOBÁ PAMÄŤ
    # ============================================================
    def store(self, key: str, value: str):
        """Uloží hodnotu do dlhodobej pamäte."""
        self.persistent_memory[key] = value

    def recall(self, key: str) -> str | None:
        """Vráti hodnotu z dlhodobej pamäte."""
        return self.persistent_memory.get(key)

    # ============================================================
    #  PREKLAD (PRIPRAVENÉ)
    # ============================================================
    def translate(self, text: str, target_lang: str = "en") -> str:
        """Placeholder pre prekladový modul."""
        return f"[translate → {target_lang}] {text}"

    # ============================================================
    #  STAV SYSTÉMU
    # ============================================================
    def set_state(self, key: str, value: str):
        """Nastaví stavový parameter systému."""
        self.state[key] = value

    def get_state(self, key: str) -> str | None:
        """Vráti stavový parameter systému."""
        return self.state.get(key)

    # ============================================================
    #  VALIDÁCIA KONTEXTU
    # ============================================================
    def validate(self) -> bool:
        """
        Overí, či je kontext v konzistentnom stave.
        Toto je základ pre budúci Workflow Engine.
        """
        if not isinstance(self.session_memory, list):
            return False
        if not isinstance(self.persistent_memory, dict):
            return False
        if not isinstance(self.state, dict):
            return False
        return True

    # ============================================================
    #  SNAPSHOTS / HISTÓRIA
    # ============================================================
    def snapshot(self):
        """Uloží aktuálny stav kontextu do histórie."""
        snap = {
            "session": list(self.session_memory),
            "persistent": dict(self.persistent_memory),
            "state": dict(self.state),
        }
        self.history.append(snap)

        # Limit histórie
        if len(self.history) > self.max_history:
            self.history.pop(0)

    def rollback(self, steps: int = 1):
        """Vráti kontext o N krokov späť."""
        if steps <= 0 or steps > len(self.history):
            return False

        snap = self.history[-steps]
        self.session_memory = list(snap["session"])
        self.persistent_memory = dict(snap["persistent"])
        self.state = dict(snap["state"])

        return True

    # ============================================================
    #  DIFF / MERGE
    # ============================================================
    def diff(self, other_state: dict) -> dict:
        """
        Porovná aktuálny stav s iným stavom.
        Použiteľné pre AITE a Workflow Engine.
        """
        differences = {}
        for key, value in other_state.items():
            if self.state.get(key) != value:
                differences[key] = {
                    "current": self.state.get(key),
                    "incoming": value
                }
        return differences

    def merge(self, new_state: dict):
        """
        Bezpečne zlúči nový stav so starým.
        """
        for key, value in new_state.items():
            self.state[key] = value
