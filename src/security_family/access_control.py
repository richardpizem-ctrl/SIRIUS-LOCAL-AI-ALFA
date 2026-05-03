# SECURITY FAMILY – Access Control 3.0
# Dynamic permissions based on identity, context, and risk score.

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
            "time_limit_exceeded": bool
        }
        """

        base = self.base_levels.get(identity, self.base_levels["STRANGER"])
        permissions = set(base["permissions"])

        if context:
            permissions |= self._apply_context_rules(identity, context)

        return sorted(list(permissions))

    # ---------------------------------------------------------
    # CONTEXT RULES
    # ---------------------------------------------------------
    def _apply_context_rules(self, identity, ctx):
        extra = set()

        # 1. High risk → restrict everything except safe ops
        if ctx.get("risk_score", 0) > 0.7:
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
