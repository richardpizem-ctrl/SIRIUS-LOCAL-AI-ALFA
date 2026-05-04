# SECURITY FAMILY – Access Control 4.0
# Dynamic permissions based on identity, context, risk score, trends, and adaptive learning.

import math
from statistics import mean

class AccessControl:
    def __init__(self):
        # Base permissions for each identity
        self.base_levels = {
            "OWNER": {
                "tier": "FULL",
                "permissions": [
                    "full_access",
                    "system_operations",
                    "sensitive_actions",
                    "module_management"
                ]
            },
            "FAMILY": {
                "tier": "LIMITED",
                "permissions": [
                    "games",
                    "media",
                    "safe_operations",
                    "school_mode_allowed"
                ]
            },
            "STRANGER": {
                "tier": "RESTRICTED",
                "permissions": [
                    "restricted_mode",
                    "no_sensitive_actions"
                ]
            }
        }

        # Adaptive learning memory
        self.history = {
            "OWNER": [],
            "FAMILY": [],
            "GLOBAL": []
        }

        self.max_short = 20
        self.max_long = 200

        # Thresholds for anomaly detection
        self.risk_threshold = 0.7
        self.anomaly_similarity_threshold = 0.35
        self.anomaly_shift_threshold = 0.25

    # ---------------------------------------------------------
    # MAIN ACCESS DECISION
    # ---------------------------------------------------------
    def get_permissions(self, identity, context=None):
        """
        identity: OWNER / FAMILY / STRANGER
        context: {
            "risk_score": float,
            "task_type": str,
            "time_of_day": int,
            "school_mode": bool,
            "time_limit_exceeded": bool,
            "behavior_vector": dict,
            "owner_similarity": float,
            "family_similarity": float
        }
        """

        base = self.base_levels.get(identity, self.base_levels["STRANGER"])
        permissions = set(base["permissions"])

        if context:
            # Update trends
            if "behavior_vector" in context:
                self._update_history("GLOBAL", context["behavior_vector"])

            # Apply contextual rules
            permissions |= self._apply_context_rules(identity, context)

            # Apply anomaly restrictions
            anomaly = self._detect_anomaly(context)
            if anomaly["is_anomaly"]:
                permissions |= {"restricted_mode", "no_sensitive_actions"}

        return sorted(list(permissions))

    # ---------------------------------------------------------
    # CONTEXT RULES
    # ---------------------------------------------------------
    def _apply_context_rules(self, identity, ctx):
        extra = set()

        # 1. High risk → restrict everything except safe ops
        if ctx.get("risk_score", 0) > self.risk_threshold:
            extra |= {"restricted_mode", "no_sensitive_actions"}
            return extra

        # 2. School mode → FAMILY gets extra permissions
        if identity == "FAMILY" and ctx.get("school_mode"):
            extra |= {"school_tools", "homework_priority"}

        # 3. Time limit exceeded → FAMILY downgraded
        if identity == "FAMILY" and ctx.get("time_limit_exceeded"):
            extra |= {"restricted_mode", "no_sensitive_actions"}

        # 4. OWNER always allowed system operations unless high risk
        if identity == "OWNER":
            extra |= {"system_operations", "sensitive_actions"}

        return extra

    # ---------------------------------------------------------
    # ADAPTIVE LEARNING (Access Control 4.0)
    # ---------------------------------------------------------
    def learn(self, identity, behavior_vector, learning_rate=0.15):
        """
        Adaptive permission learning based on long-term behavior.
        """
        if identity not in ("OWNER", "FAMILY"):
            return

        self._update_history(identity, behavior_vector)

        # Future: dynamic permission evolution
        # (placeholder for v4.1+)
        # Example: if FAMILY consistently behaves safely → unlock more safe ops
        # Example: if OWNER shows risky patterns → temporarily reduce sensitive actions

    # ---------------------------------------------------------
    # HISTORY & TRENDS
    # ---------------------------------------------------------
    def _update_history(self, label, vector):
        if label not in self.history:
            self.history[label] = []

        self.history[label].append(vector)

        if len(self.history[label]) > self.max_long:
            self.history[label] = self.history[label][-self.max_long:]

    def _compute_trends(self, label):
        records = self.history.get(label, [])
        if not records:
            return {"short": {}, "long": {}, "delta": {}}

        short = records[-self.max_short:]
        long = records

        def avg(vectors):
            keys = set().union(*vectors)
            return {k: mean([v.get(k, 0) for v in vectors]) for k in keys}

        short_avg = avg(short)
        long_avg = avg(long)

        delta = {k: short_avg.get(k, 0) - long_avg.get(k, 0)
                 for k in set(short_avg) | set(long_avg)}

        return {"short": short_avg, "long": long_avg, "delta": delta}

    # ---------------------------------------------------------
    # ANOMALY DETECTION (Access Control 4.0)
    # ---------------------------------------------------------
    def _detect_anomaly(self, ctx):
        """
        Detects:
        - low similarity to OWNER/FAMILY
        - sudden behavior shift vs long-term trend
        - high risk score
        """

        behavior = ctx.get("behavior_vector", {})
        owner_sim = ctx.get("owner_similarity", 0)
        family_sim = ctx.get("family_similarity", 0)
        risk = ctx.get("risk_score", 0)

        trends = self._compute_trends("GLOBAL")
        delta = trends["delta"]

        shift = math.sqrt(sum(v * v for v in delta.values()))

        low_similarity = max(owner_sim, family_sim) < self.anomaly_similarity_threshold
        big_shift = shift > self.anomaly_shift_threshold
        high_risk = risk > self.risk_threshold

        is_anomaly = low_similarity or big_shift or high_risk

        if is_anomaly:
            if high_risk:
                reason = "high_risk"
            elif low_similarity and big_shift:
                reason = "low_similarity_and_behavior_shift"
            elif low_similarity:
                reason = "low_similarity"
            else:
                reason = "behavior_shift"
        else:
            reason = "normal"

        return {
            "is_anomaly": is_anomaly,
            "reason": reason,
            "trend_delta": delta,
            "risk": risk,
            "similarity": {
                "OWNER": owner_sim,
                "FAMILY": family_sim
            }
        }
