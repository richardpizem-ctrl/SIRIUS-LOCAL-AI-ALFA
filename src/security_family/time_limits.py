# SECURITY FAMILY – Time Limits 3.0
# Intelligent time-based safety for FAMILY profiles.

import time

class TimeLimits:
    def __init__(self, config=None):
        """
        config example:
        {
            "child_1": {
                "chat_minutes": 30,
                "games_minutes": 60,
                "media_minutes": 45
            }
        }
        """
        self.config = config or {}
        self.sessions = {}  # {user_id: {session_type: start_timestamp}}

    # ---------------------------------------------------------
    # SESSION CONTROL
    # ---------------------------------------------------------
    def start_session(self, user_id, session_type):
        """Start tracking a new session."""
        if user_id not in self.sessions:
            self.sessions[user_id] = {}

        self.sessions[user_id][session_type] = time.time()

    def get_remaining_time(self, user_id, session_type):
        """Return remaining allowed time in minutes."""
        if user_id not in self.sessions:
            return self._get_limit(user_id, session_type)

        if session_type not in self.sessions[user_id]:
            return self._get_limit(user_id, session_type)

        start = self.sessions[user_id][session_type]
        elapsed_minutes = (time.time() - start) / 60
        limit = self._get_limit(user_id, session_type)

        return max(0, limit - elapsed_minutes)

    # ---------------------------------------------------------
    # WARNINGS & ENFORCEMENT
    # ---------------------------------------------------------
    def should_warn(self, user_id, session_type, threshold=5):
        """
        Return True if remaining time is below threshold minutes.
        Default: warn 5 minutes before end.
        """
        remaining = self.get_remaining_time(user_id, session_type)
        return remaining <= threshold and remaining > 0

    def should_end(self, user_id, session_type):
        """Return True if session should be ended."""
        return self.get_remaining_time(user_id, session_type) <= 0

    # ---------------------------------------------------------
    # INTERNAL HELPERS
    # ---------------------------------------------------------
    def _get_limit(self, user_id, session_type):
        """Return configured limit for a child."""
        user_cfg = self.config.get(user_id, {})
        return user_cfg.get(f"{session_type}_minutes", 0)
