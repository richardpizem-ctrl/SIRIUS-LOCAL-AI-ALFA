# SECURITY FAMILY – Stranger Mode 3.0
# Activated when behavior does not match OWNER or FAMILY.
# Provides isolation, safe mode, and restricted access.

class StrangerMode:
    def __init__(self, access_control, behavior_audit):
        self.access_control = access_control
        self.behavior_audit = behavior_audit
        self.active = False

    # ---------------------------------------------------------
    # MAIN ACTIVATION
    # ---------------------------------------------------------
    def activate(self, behavior_data=None):
        """
        Restrict access to sensitive operations.
        Triggered when:
            - behavior does not match OWNER/FAMILY
            - risk score is high
            - identity is uncertain
        """

        self.active = True

        # 1. Calculate risk score
        risk = self._calculate_risk(behavior_data)

        # 2. Build context for AccessControl
        context = {
            "risk_score": risk,
            "school_mode": False,
            "time_limit_exceeded": False
        }

        # 3. Get restricted permissions
        permissions = self.access_control.get_permissions("STRANGER", context)

        # 4. Return full StrangerMode state
        return {
            "mode": "STRANGER_MODE",
            "risk_score": risk,
            "permissions": permissions,
            "safe_mode": True,
            "isolation": {
                "fs_agent": True,
                "win_cap": True,
                "workflow_engine": True,
                "plugins": True
            }
        }

    # ---------------------------------------------------------
    # INTERNAL RISK CALCULATION
    # ---------------------------------------------------------
    def _calculate_risk(self, behavior_data):
        """Convert behavior audit into a risk score."""
        if not behavior_data:
            return 1.0  # No data = maximum risk

        scores = self.behavior_audit.audit(behavior_data)

        # Stranger score is already computed in BehaviorAudit
        return scores.get("STRANGER", 1.0)
