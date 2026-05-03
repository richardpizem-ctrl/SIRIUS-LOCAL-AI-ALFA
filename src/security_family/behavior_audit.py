# SECURITY FAMILY – Behavior Audit
# Continuously compares current behavior with stored profiles.

import math
from statistics import mean

class BehaviorAudit:
    def __init__(self, profile_store):
        self.profile_store = profile_store

    def audit(self, data):
        """
        Returns confidence score for OWNER/FAMILY/STRANGER.
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

        owner_score = self._compare_profiles(data, owner)
        family_score = self._compare_profiles(data, family)
        stranger_score = self._stranger_score(data, owner, family)

        return {
            "OWNER": owner_score,
            "FAMILY": family_score,
            "STRANGER": stranger_score
        }

    # ---------------------------------------------------------
    # INTERNAL METHODS
    # ---------------------------------------------------------

    def _compare_profiles(self, data, profile):
        """Cosine similarity between current behavior and stored profile."""
        if not profile:
            return 0.0

        keys = set(data.keys()) & set(profile.keys())
        if not keys:
            return 0.0

        v1 = [data[k] for k in keys]
        v2 = [profile[k] for k in keys]

        dot = sum(a*b for a, b in zip(v1, v2))
        mag1 = math.sqrt(sum(a*a for a in v1))
        mag2 = math.sqrt(sum(b*b for b in v2))

        if mag1 == 0 or mag2 == 0:
            return 0.0

        return dot / (mag1 * mag2)

    def _stranger_score(self, data, owner, family):
        """Higher score = more likely stranger."""
        # If behavior is far from both profiles → stranger
        owner_sim = self._compare_profiles(data, owner)
        family_sim = self._compare_profiles(data, family)

        # Stranger = inverse similarity
        return 1 - max(owner_sim, family_sim)
