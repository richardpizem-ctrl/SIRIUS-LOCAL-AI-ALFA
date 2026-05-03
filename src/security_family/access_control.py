# SECURITY FAMILY – Access Control
# Defines permissions for OWNER, FAMILY, and STRANGER.

class AccessControl:
    def __init__(self):
        self.levels = {
            "OWNER": ["full_access"],
            "FAMILY": ["games", "media", "safe_operations"],
            "STRANGER": ["restricted_mode"]
        }

    def get_permissions(self, identity):
        return self.levels.get(identity, ["restricted_mode"])
