# SECURITY FAMILY – Family Mode 4.0
# Safe environment for children of the owner.
# Integrates with AccessControl 4.0, BehaviorAudit 4.0, Time Limits, and Trend Engine.

import math

class FamilyMode:
    def __init__(self, access_control, behavior_audit, time_limits):
        self.access_control = access_control
        self.behavior_audit = behavior_audit
        self.time_limits = time_limits

        self.active = False
        self.school_mode = False

        # Behavior history for trends
        self.history = []
        self.max_short = 20
        self.max_long = 200

        # Thresholds
        self.safe_mode_threshold = 0.65   # stranger score threshold
        self.anomaly_penalty = 0.25       # extra risk added when anomaly detected

    # ---------------------------------------------------------
    # MAIN ACTIVATION
    # ---------------------------------------------------------
    def activate(self, behavior_data=None):
        """
        Enable safe games, multimedia, and non-destructive actions.
        Automatically adjusts based on:
            - behavior confidence
            - time limits
            - school mode
            - anomaly detection
            - behavior trends
        """

        self.active = True

        # 1. Behavior audit → risk score
        risk, audit_scores, anomaly = self._calculate_risk(behavior_data)

        # 2. Time limit enforcement
        time_exceeded = self.time_limits.exceeded("FAMILY")

        # 3. Build context for AccessControl 4.0
        context = {
            "risk_score": risk,
            "school_mode": self.school_mode,
            "time_limit_exceeded": time_exceeded,
            "behavior_vector": behavior_data,
            "owner_similarity": audit_scores.get("OWNER", 0),
            "family_similarity": audit_scores.get("FAMILY", 0)
        }

        # 4. Get dynamic permissions
        permissions = self.access_control.get_permissions("FAMILY", context)

        # 5. Determine mode (FAMILY_MODE vs SAFE_MODE)
        mode = "SAFE_MODE" if risk > self.safe_mode_threshold else "FAMILY_MODE"

        return {
            "mode": mode,
            "school_mode": self.school_mode,
            "risk_score": risk,
            "anomaly": anomaly,
            "time_limit_exceeded": time_exceeded,
            "permissions": permissions
        }

    # ---------------------------------------------------------
    # SCHOOL MODE
    # ---------------------------------------------------------
    def enable_school_mode(self):
        """Prioritize homework, disable games, allow school tools."""
        self.school_mode = True

    def disable_school_mode(self):
        self.school_mode = False

    # ---------------------------------------------------------
    # INTERNAL RISK CALCULATION (Family Mode 4.0)
    # ---------------------------------------------------------
    def _calculate_risk(self, behavior_data):
        """Convert behavior audit into a risk score with anomaly detection and trends."""
        if not behavior_data:
            return 0.0, {}, {"is_anomaly": False}

        # 1. Behavior audit
        audit_scores = self.behavior_audit.audit(behavior_data)
        family_score = audit_scores.get("FAMILY", 0)
        stranger_score = audit_scores.get("STRANGER", 0)

        # 2. Update history for trends
        self._update_history(behavior_data)
        trends = self._compute_trends()

        # 3. Detect anomaly
        anomaly = self._detect_anomaly(audit_scores, trends)

        # 4. Base risk = stranger score
        risk = stranger_score

        # 5. Add anomaly penalty
        if anomaly["is_anomaly"]:
            risk += self.anomaly_penalty

        # 6. Clamp to 0–1
        risk = max(0, min(1, risk))

        return risk, audit_scores, anomaly

    # ---------------------------------------------------------
    # HISTORY & TRENDS
    # ---------------------------------------------------------
    def _update_history(self, vector):
        self.history.append(vector)
        if len(self.history) > self.max_long:
            self.history = self.history[-self.max_long:]

    def _compute_trends(self):
        if not self.history:
            return {"short": {}, "long": {}, "delta": {}}

        short = self.history[-self.max_short:]
        long = self.history

        def avg(vectors):
            keys = set().union(*vectors)
            return {k: sum(v.get(k, 0) for v in vectors) / len(vectors) for k in keys}

        short_avg = avg(short)
        long_avg = avg(long)

        delta = {k: short_avg.get(k, 0) - long_avg.get(k, 0)
                 for k in set(short_avg) | set(long_avg)}

        return {"short": short_avg, "long": long_avg, "delta": delta}

    # ---------------------------------------------------------
    # ANOMALY DETECTION (Family Mode 4.0)
    # ---------------------------------------------------------
    def _detect_anomaly(self, audit_scores, trends):
        """
        Detects:
        - low FAMILY similarity
        - high STRANGER similarity
        - sudden behavior shift vs long-term trend
        """

        family_sim = audit_scores.get("FAMILY", 0)
        stranger_sim = audit_scores.get("STRANGER", 0)

        delta = trends.get("delta", {})
        shift = math.sqrt(sum(v * v for v in delta.values()))

        low_family = family_sim < 0.35
        high_stranger = stranger_sim > 0.65
        big_shift = shift > 0.25

        is_anomaly = low_family or high_stranger or big_shift

        if is_anomaly:
            if high_stranger:
                reason = "high_stranger_similarity"
            elif low_family and big_shift:
                reason = "low_family_and_behavior_shift"
            elif low_family:
                reason = "low_family_similarity"
            else:
                reason = "behavior_shift"
        else:
            reason = "normal"

        return {
            "is_anomaly": is_anomaly,
            "reason": reason,
            "trend_delta": delta,
            "similarity": {
                "FAMILY": family_sim,
                "STRANGER": stranger_sim
            }
        }
