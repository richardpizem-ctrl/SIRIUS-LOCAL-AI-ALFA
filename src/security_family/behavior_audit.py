# SECURITY FAMILY – Behavior Audit
# Continuously compares current behavior with stored profiles.
#
# Behavior Vector 3.0 – Specification
# Dimensions (normalized 0–1 before use):
#   - typing_speed      : normalized typing speed (0–300 chars/min → 0–1)
#   - command_pattern   : pattern similarity / command style (0–1)
#   - vocabulary        : lexical style / word choice (0–1)
#   - task_type         : type/category of tasks (0–1)
#   - time_of_day       : hour-of-day mapped to 0–1
#   - error_rate        : input / command error ratio (0–1)
#
# Identity logic:
#   - OWNER / FAMILY similarity via weighted cosine similarity
#   - STRANGER = 1 - max(OWNER_sim, FAMILY_sim)
#   - Adaptive learning: profiles update over time
#   - Trends: short-term vs long-term behavior history
#   - Anomaly detection: sudden deviation from both profiles and own history

import math
from statistics import mean

class BehaviorAudit:
    def __init__(self, profile_store):
        self.profile_store = profile_store

        # Váhové koeficienty – najdôležitejšie metriky majú najväčšiu váhu
        self.weights = {
            "command_pattern": 0.40,
            "typing_speed": 0.25,
            "vocabulary": 0.15,
            "task_type": 0.10,
            "error_rate": 0.05,
            "time_of_day": 0.05
        }

        # Normalizačné rozsahy (min, max) – môžeš upraviť podľa reálnych dát
        self.norm_ranges = {
            "typing_speed": (0, 300),      # znaky/min
            "command_pattern": (0, 1),     # už normalizované
            "vocabulary": (0, 1),          # už normalizované
            "task_type": (0, 1),           # už normalizované
            "time_of_day": (0, 24),        # hodiny
            "error_rate": (0, 1)           # percentuálna chyba
        }

        # Behavior history for trends (short-term vs long-term)
        # structure: {"OWNER": [vector1, vector2, ...], "FAMILY": [...], "GLOBAL": [...]}
        self.history = {
            "OWNER": [],
            "FAMILY": [],
            "GLOBAL": []
        }
        self.max_short_term = 20   # posledných N záznamov = krátkodobý trend
        self.max_long_term = 200   # dlhodobý trend (agregovaný)

        # Thresholds for anomaly detection (can be tuned)
        self.anomaly_similarity_threshold = 0.35   # low similarity to profiles
        self.anomaly_trend_delta_threshold = 0.25  # big jump vs own history

    # ---------------------------------------------------------
    # PUBLIC API
    # ---------------------------------------------------------

    def audit(self, data):
        """
        Returns confidence score for OWNER/FAMILY/STRANGER and anomaly/trend info.
        'data' = dictionary with behavior metrics:
            - typing_speed
            - command_pattern
            - vocabulary
            - task_type
            - time_of_day
            - error_rate
        """

        owner = self.profile_store.get("OWNER", {})
        family = self.profile_store.get("FAMILY", {})
        stranger = {}  # baseline = empty

        # Normalize current behavior into Behavior Vector 3.0
        behavior_vector = self._build_behavior_vector(data)

        owner_score = self._compare_profiles(behavior_vector, owner)
        family_score = self._compare_profiles(behavior_vector, family)
        stranger_score = self._stranger_score(behavior_vector, owner, family)

        # Update history for trends
        self._update_history("GLOBAL", behavior_vector)

        # Trends (short-term vs long-term)
        trends = self._compute_trends("GLOBAL")

        # Anomaly detection
        anomaly = self._detect_anomaly(
            behavior_vector,
            owner_score,
            family_score,
            trends
        )

        return {
            "OWNER": owner_score,
            "FAMILY": family_score,
            "STRANGER": stranger_score,
            "ANOMALY": anomaly,
            "TRENDS": trends
        }

    def learn(self, label, data, learning_rate=0.2):
        """
        Adaptive learning of profiles.
        label = "OWNER" | "FAMILY"
        data  = current behavior metrics (same structure as in audit()).

        This gradually updates stored profile towards new behavior.
        """
        if label not in ("OWNER", "FAMILY"):
            return

        profile = self.profile_store.get(label, {})
        vector = self._build_behavior_vector(data)

        if not profile:
            # First-time profile = direct copy
            self.profile_store[label] = vector.copy()
        else:
            # Incremental update (exponential moving average style)
            updated = {}
            for k in self.weights.keys():
                old = profile.get(k, vector.get(k, 0.0))
                new = vector.get(k, old)
                updated[k] = (1 - learning_rate) * old + learning_rate * new
            self.profile_store[label] = updated

        # Update history for this identity
        self._update_history(label, vector)

    # ---------------------------------------------------------
    # INTERNAL METHODS – CORE
    # ---------------------------------------------------------

    def _build_behavior_vector(self, data):
        """Builds normalized Behavior Vector 3.0 from raw data dict."""
        vector = {}
        for k in self.weights.keys():
            if k in data:
                vector[k] = self._normalize(k, data[k])
        return vector

    def _normalize(self, key, value):
        """Normalizuje hodnotu na rozsah 0–1 podľa definovaných rozsahov."""
        if key not in self.norm_ranges:
            return value  # fallback

        min_v, max_v = self.norm_ranges[key]
        if max_v - min_v == 0:
            return 0

        norm = (value - min_v) / (max_v - min_v)
        return max(0, min(1, norm))  # clipping

    def _compare_profiles(self, vector, profile):
        """Weighted cosine similarity between current behavior and stored profile."""
        if not profile:
            return 0.0

        keys = set(vector.keys()) & set(profile.keys()) & set(self.weights.keys())
        if not keys:
            return 0.0

        v1 = [vector[k] for k in keys]
        v2 = [profile[k] for k in keys]
        w  = [self.weights[k] for k in keys]

        dot = sum(a * b * weight for a, b, weight in zip(v1, v2, w))
        mag1 = math.sqrt(sum((a * weight) ** 2 for a, weight in zip(v1, w)))
        mag2 = math.sqrt(sum((b * weight) ** 2 for b, weight in zip(v2, w)))

        if mag1 == 0 or mag2 == 0:
            return 0.0

        return dot / (mag1 * mag2)

    def _stranger_score(self, vector, owner, family):
        """Higher score = more likely stranger."""
        owner_sim = self._compare_profiles(vector, owner)
        family_sim = self._compare_profiles(vector, family)
        return 1 - max(owner_sim, family_sim)

    # ---------------------------------------------------------
    # INTERNAL METHODS – HISTORY & TRENDS
    # ---------------------------------------------------------

    def _update_history(self, label, vector):
        """Append behavior vector to history and keep bounded size."""
        if label not in self.history:
            self.history[label] = []

        self.history[label].append(vector)

        # Bound short-term and long-term implicitly by trimming
        if len(self.history[label]) > self.max_long_term:
            self.history[label] = self.history[label][-self.max_long_term:]

    def _compute_trends(self, label):
        """
        Returns short-term and long-term average vectors and their divergence.
        {
          "short_term_avg": {...},
          "long_term_avg": {...},
          "delta": {...}
        }
        """
        records = self.history.get(label, [])
        if not records:
            return {
                "short_term_avg": {},
                "long_term_avg": {},
                "delta": {}
            }

        # Short-term = last N
        short = records[-self.max_short_term:]
        long = records  # all (already bounded)

        def avg_vector(vectors):
            if not vectors:
                return {}
            keys = set().union(*[v.keys() for v in vectors])
            result = {}
            for k in keys:
                vals = [v.get(k, 0.0) for v in vectors]
                result[k] = mean(vals)
            return result

        short_avg = avg_vector(short)
        long_avg = avg_vector(long)

        delta = {}
        for k in set(short_avg.keys()) | set(long_avg.keys()):
            delta[k] = short_avg.get(k, 0.0) - long_avg.get(k, 0.0)

        return {
            "short_term_avg": short_avg,
            "long_term_avg": long_avg,
            "delta": delta
        }

    # ---------------------------------------------------------
    # INTERNAL METHODS – ANOMALY DETECTION
    # ---------------------------------------------------------

    def _detect_anomaly(self, vector, owner_sim, family_sim, trends):
        """
        Returns anomaly info:
        {
          "is_anomaly": bool,
          "reason": str,
          "similarity": {"OWNER": x, "FAMILY": y},
          "trend_delta": {...}
        }
        """
        max_sim = max(owner_sim, family_sim)
        delta = trends.get("delta", {})

        # Magnitude of behavior shift vs long-term
        shift_magnitude = math.sqrt(sum(v * v for v in delta.values()))

        is_low_similarity = max_sim < self.anomaly_similarity_threshold
        is_big_shift = shift_magnitude > self.anomaly_trend_delta_threshold

        is_anomaly = is_low_similarity or is_big_shift

        if is_anomaly:
            if is_low_similarity and is_big_shift:
                reason = "low_similarity_and_behavior_shift"
            elif is_low_similarity:
                reason = "low_similarity_to_profiles"
            else:
                reason = "sudden_behavior_shift"
        else:
            reason = "normal"

        return {
            "is_anomaly": is_anomaly,
            "reason": reason,
            "similarity": {
                "OWNER": owner_sim,
                "FAMILY": family_sim
            },
            "trend_delta": delta
        }
