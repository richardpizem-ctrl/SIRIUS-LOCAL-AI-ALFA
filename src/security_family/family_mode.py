# SECURITY FAMILY – Family Mode 3.0
# Safe environment for children of the owner.
# Integrates with AccessControl, BehaviorAudit, and Time Limits.

class FamilyMode:
    def __init__(self, access_control, behavior_audit, time_limits):
        self.access_control = access_control
        self.behavior_audit = behavior_audit
        self.time_limits = time_limits

        self.active = False
        self.school_mode = False

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
        """

        self.active = True

        # 1. Behavior check (if child behaves unusually → safe mode)
        risk = self._calculate_risk(behavior_data)

        # 2. Time limit enforcement
        time_exceeded = self.time_limits.exceeded("FAMILY")

        # 3. Build context for AccessControl
        context = {
            "risk_score": risk,
            "school_mode": self.school_mode,
            "time_limit_exceeded": time_exceeded
        }

        # 4. Get dynamic permissions
        permissions = self.access_control.get_permissions("FAMILY", context)

        return {
            "mode": "FAMILY_MODE",
            "school_mode": self.school_mode,
            "risk_score": risk,
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
    # INTERNAL RISK CALCULATION
    # ---------------------------------------------------------
    def _calculate_risk(self, behavior_data):
        """Convert behavior audit into a risk score."""
        if not behavior_data:
            return 0.0

        scores = self.behavior_audit.audit(behavior_data)

        # FAMILY should match family profile strongly
        family_score = scores.get("FAMILY", 0)
        stranger_score = scores.get("STRANGER", 0)

        # Risk = how close behavior is to stranger
        return stranger_score
