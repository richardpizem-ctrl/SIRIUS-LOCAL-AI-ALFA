class ContextManager:
    """
    ContextManager 4.0
    Manages the internal AI context for SIRIUS LOCAL AI.

    Features:
    - short‑term memory (session)
    - long‑term memory (persistent)
    - system state
    - snapshot history with capacity limit
    - validation
    - rollback
    - diff and merge utilities
    - safe deep-copy operations
    """

    def __init__(self):
        # ---------------------------------------------------------
        # MEMORY STRUCTURES
        # ---------------------------------------------------------
        self.session_memory: list[str] = []
        self.persistent_memory: dict[str, str] = {}
        self.state: dict[str, str] = {}

        # ---------------------------------------------------------
        # SNAPSHOT HISTORY
        # ---------------------------------------------------------
        self.history: list[dict] = []
        self.max_history = 20

    # ============================================================
    #  SHORT‑TERM MEMORY
    # ============================================================
    def remember(self, text: str):
        """Append a new item to session memory."""
        self.session_memory.append(text)

    def get_recent(self, limit: int = 5) -> list[str]:
        """Return the last N items from session memory."""
        return self.session_memory[-limit:]

    # ============================================================
    #  LONG‑TERM MEMORY
    # ============================================================
    def store(self, key: str, value: str):
        """Store a key-value pair in persistent memory."""
        self.persistent_memory[key] = value

    def recall(self, key: str) -> str | None:
        """Retrieve a value from persistent memory."""
        return self.persistent_memory.get(key)

    # ============================================================
    #  TRANSLATION (placeholder)
    # ============================================================
    def translate(self, text: str, target_lang: str = "en") -> str:
        """Placeholder translation method."""
        return f"[translate → {target_lang}] {text}"

    # ============================================================
    #  STATE MANAGEMENT
    # ============================================================
    def set_state(self, key: str, value: str):
        """Set a state variable."""
        self.state[key] = value

    def get_state(self, key: str) -> str | None:
        """Retrieve a state variable."""
        return self.state.get(key)

    # ============================================================
    #  VALIDATION
    # ============================================================
    def validate(self) -> bool:
        """Validate internal structures and snapshot integrity."""
        if not isinstance(self.session_memory, list):
            return False
        if not isinstance(self.persistent_memory, dict):
            return False
        if not isinstance(self.state, dict):
            return False
        if not isinstance(self.history, list):
            return False

        # Validate snapshots
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
        """Create a snapshot of the current context."""
        snap = {
            "session": list(self.session_memory),
            "persistent": dict(self.persistent_memory),
            "state": dict(self.state),
        }
        self.history.append(snap)

        # Enforce capacity
        if len(self.history) > self.max_history:
            self.history.pop(0)

    # ============================================================
    #  ROLLBACK
    # ============================================================
    def rollback(self, steps: int = 1):
        """
        Roll back the context by N snapshots.
        Returns True on success, False on invalid request.
        """
        if steps <= 0 or steps > len(self.history):
            return False

        snap = self.history[-steps]

        self.session_memory = list(snap["session"])
        self.persistent_memory = dict(snap["persistent"])
        self.state = dict(snap["state"])

        # Remove snapshots after rollback point
        del self.history[-steps+1:]

        return True

    # ============================================================
    #  DIFF
    # ============================================================
    def diff(self, other_state: dict) -> dict:
        """
        Compare current state with another state dictionary.
        Returns a dict of differences.
        """
        differences = {}

        # Keys in other_state
        for key, value in other_state.items():
            if self.state.get(key) != value:
                differences[key] = {
                    "current": self.state.get(key),
                    "incoming": value
                }

        # Keys missing in other_state
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
        """
        Safely merge new state values into the current state.
        """
        for key, value in new_state.items():
            if isinstance(key, str):
                self.state[key] = value
