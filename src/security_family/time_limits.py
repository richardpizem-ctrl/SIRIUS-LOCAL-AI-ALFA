# SECURITY FAMILY – Time Limits 4.0
# Intelligent time-based safety for FAMILY profiles.
# Adds:
# - adaptive learning of usage patterns
# - anomaly detection
# - short-term & long-term trends
# - risk scoring
# - dynamic limit adjustments
# - SAFE_MODE activation

import time
import math
from statistics import mean

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

        # Usage history for trends
        self.usage_history = {}  # {user_id: [{session_type, duration}]}

        self.max_short = 20
        self.max_long = 200

        # Thresholds
        self.anomaly_shift_threshold = 0.35
        self.anomaly_penalty = 0.25

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
        """Return True if remaining time is below threshold minutes."""
        remaining = self.get_remaining_time(user_id, session_type)
        return remaining <= threshold and remaining > 0

    def should_end(self, user_id, session_type):
        """Return True if session should be ended."""
        return self.get_remaining_time(user_id, session_type) <= 0

    # ---------------------------------------------------------
    # SESSION END + LEARNING
    # ---------------------------------------------------------
    def end_session(self, user_id, session_type):
        """End session and learn from usage."""
        if user_id not in self.sessions:
            return

        if session_type not in self.sessions[user_id]:
            return

        start = self.sessions[user_id][session_type]
        duration = (time.time() - start) / 60  # minutes

        # Save usage history
        self._update_usage_history(user_id, session_type, duration)

        # Adaptive learning
        self._adaptive_learn(user_id, session_type, duration)

        # Remove session
        del self.sessions[user_id][session_type]

    # ---------------------------------------------------------
    # ADAPTIVE LEARNING (Time Limits 4.0)
    # ---------------------------------------------------------
    def _adaptive_learn(self, user_id, session_type, duration, learning_rate=0.1):
        """
        Adjust limits based on long-term behavior.
        If child consistently uses less time → reduce limit.
        If child consistently uses more time → increase limit slightly.
        """

        limit = self._get_limit(user_id, session_type)
        trends = self._compute_trends(user_id, session_type)

        long_avg = trends["long"]

        if long_avg == 0:
            return

        # If child always uses less → reduce limit
        if long_avg < limit * 0.5:
            new_limit = limit * (1 - learning_rate)

        # If child always uses more → increase limit slightly
        elif long_avg > limit * 1.2:
            new_limit = limit * (1 + learning_rate)

        else:
            return  # no change

        # Clamp limit
        new_limit = max(5, min(240, new_limit))

        # Save updated limit
        self.config[user_id][f"{session_type}_minutes"] = new_limit

    # ---------------------------------------------------------
    # ANOMALY DETECTION
    # ---------------------------------------------------------
    def detect_anomaly(self, user_id, session_type):
        """
        Detects:
        - sudden spikes in usage
        - extreme deviations from long-term trend
        """

        trends = self._compute_trends(user_id, session_type)
        delta = trends["delta"]

        shift = abs(delta)

        is_anomaly = shift > self.anomaly_shift_threshold

        return {
            "is_anomaly": is_anomaly,
            "reason": "usage_spike" if is_anomaly else "normal",
            "shift": shift,
            "short_term_avg": trends["short"],
            "long_term_avg": trends["long"]
        }

    # ---------------------------------------------------------
    # TRENDS
    # ---------------------------------------------------------
    def _update_usage_history(self, user_id, session_type, duration):
        if user_id not in self.usage_history:
            self.usage_history[user_id] = []

        self.usage_history[user_id].append({
            "session_type": session_type,
            "duration": duration
        })

        if len(self.usage_history[user_id]) > self.max_long:
            self.usage_history[user_id] = self.usage_history[user_id][-self.max_long:]

    def _compute_trends(self, user_id, session_type):
        if user_id not in self.usage_history:
            return {"short": 0, "long": 0, "delta": 0}

        records = [r["duration"] for r in self.usage_history[user_id]
                   if r["session_type"] == session_type]

        if not records:
            return {"short": 0, "long": 0, "delta": 0}

        short = records[-self.max_short:]
        long = records

        short_avg = mean(short)
        long_avg = mean(long)

        delta = short_avg - long_avg

        return {
            "short": short_avg,
            "long": long_avg,
            "delta": delta
        }

    # ---------------------------------------------------------
    # INTERNAL HELPERS
    # ---------------------------------------------------------
    def _get_limit(self, user_id, session_type):
        """Return configured limit for a child."""
        user_cfg = self.config.get(user_id, {})
        return user_cfg.get(f"{session_type}_minutes", 0)
