# SECURITY FAMILY – Time Limits
# Time-based safety for FAMILY profiles (children).

class TimeLimits:
    def __init__(self, config=None):
        self.config = config or {}
        # example: {"chat_minutes": 30, "games_minutes": 60}

    def start_session(self, user_id, session_type):
        """Start tracking a new session (chat, games, etc.)."""
        pass

    def get_remaining_time(self, user_id, session_type):
        """Return remaining allowed time in minutes."""
        pass

    def should_warn(self, user_id, session_type):
        """Return True if it's time to warn the child."""
        pass

    def should_end(self, user_id, session_type):
        """Return True if session should be ended."""
        pass
