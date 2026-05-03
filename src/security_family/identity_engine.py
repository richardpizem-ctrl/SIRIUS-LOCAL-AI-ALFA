# SECURITY FAMILY – Identity Engine 3.0
# Learns and recognizes OWNER and FAMILY behavior profiles.

import math

class IdentityEngine:
    def __init__(self, profile_store):
        self.profile_store = profile_store

    # ---------------------------------------------------------
    # LEARNING
    # ---------------------------------------------------------

    def learn_owner(self, data):
        """Initial or incremental learning for OWNER profile."""
        self._update_profile("OWNER", data)

    def learn_family_member(self, data, member_id="default"):
        """
        Learning behavior patterns for children.
        Each child can have their own profile.
        """
        key = f"FAMILY_{member_id}"
        self._update_profile(key, data)

    # ---------------------------------------------------------
    # IDENTIFICATION
    # ---------------------------------------------------------

    def identify_user(self, data):
        """
        Returns: 'OWNER', 'FAMILY', or 'STRANGER'
        Based on similarity to stored profiles.
        """

        scores = {}

        # Compare with OWNER
        owner_profile = self.profile_store.get("OWNER", {})
        scores["OWNER"] = self._similarity(data, owner_profile)

        # Compare with all FAMILY profiles
        family_scores = []
        for key, profile in self.profile_store.items():
            if key.startswith("FAMILY_"):
                family_scores.append(self._similarity(data, profile))

        scores["FAMILY"] = max(family_scores) if family_scores else 0.0

        # Stranger score = inverse similarity
        scores["STRANGER"] = 1 - max(scores["OWNER"], scores["FAMILY"])

        # Decide identity
        identity = max(scores, key=scores.get)
        return identity, scores

    # ---------------------------------------------------------
    # INTERNAL METHODS
    # ---------------------------------------------------------

    def _update_profile(self, key, data):
        """
        Incrementally updates a behavior profile.
        Uses weighted averaging to avoid sudden jumps.
        """

        existing = self.profile_store.get(key, {})

        updated = {}
        for k, v in data.items():
            if k in existing:
                # Weighted update (80% old, 20% new)
                updated[k] = (existing[k] * 0.8) + (v * 0.2)
            else:
                updated[k] = v

        self.profile_store[key] = updated

    def _similarity(self, data, profile):
        """Cosine similarity between behavior vectors."""
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
