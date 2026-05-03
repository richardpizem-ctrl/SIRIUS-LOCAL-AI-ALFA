# SECURITY FAMILY – Behavior Audit
# Continuously compares current behavior with stored profiles.

class BehaviorAudit:
    def __init__(self, profile_store):
        self.profile_store = profile_store

    def audit(self, data):
        """Returns confidence score for OWNER/FAMILY/STRANGER."""
        pass
