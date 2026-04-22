class ContextManager:
    """
    Spravuje kontext SIRIUS LOCAL AI ALFA.
    Obsahuje:
    - krátkodobú pamäť (session memory)
    - dlhodobú pamäť (persistent memory)
    - prekladové funkcie (pripravené)
    - stav systému
    """

    def __init__(self):
        self.session_memory: list[str] = []
        self.persistent_memory: dict[str, str] = {}
        self.state: dict[str, str] = {}

    # -----------------------------
    #  KRÁTKODOBÁ PAMÄŤ
    # -----------------------------
    def remember(self, text: str):
        """Uloží text do krátkodobej pamäte."""
        self.session_memory.append(text)

    def get_recent(self, limit: int = 5) -> list[str]:
        """Vráti posledné položky z krátkodobej pamäte."""
        return self.session_memory[-limit:]

    # -----------------------------
    #  DLHODOBÁ PAMÄŤ
    # -----------------------------
    def store(self, key: str, value: str):
        """Uloží hodnotu do dlhodobej pamäte."""
        self.persistent_memory[key] = value

    def recall(self, key: str) -> str | None:
        """Vráti hodnotu z dlhodobej pamäte."""
        return self.persistent_memory.get(key)

    # -----------------------------
    #  PREKLAD (PRIPRAVENÉ)
    # -----------------------------
    def translate(self, text: str, target_lang: str = "en") -> str:
        """
        Placeholder pre prekladový modul.
        Neskôr sa sem doplní reálna implementácia.
        """
        return f"[translate → {target_lang}] {text}"

    # -----------------------------
    #  STAV SYSTÉMU
    # -----------------------------
    def set_state(self, key: str, value: str):
        self.state[key] = value

    def get_state(self, key: str) -> str | None:
        return self.state.get(key)
