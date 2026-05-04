    # ============================================================
    #  SEND EMAIL (FINAL v4.0 PIPELINE)
    # ============================================================

    def send_email(self, draft: dict, sender_profile: dict | None = None):
        """
        Final v4.0 send-email pipeline.
        Converts a draft into a sent email, validates it,
        attaches sender profile, timestamps it, and stores it.
        """

        # -----------------------------
        # VALIDATE DRAFT FIELDS
        # -----------------------------
        validation = self.validator.validate_full(
            draft.get("to", ""),
            draft.get("subject", ""),
            draft.get("body", "")
        )

        if not validation["all_valid"]:
            return {
                "status": "error",
                "message": "Draft validation failed.",
                "details": validation
            }

        # -----------------------------
        # COPY DRAFT → SENT EMAIL
        # -----------------------------
        sent = copy.deepcopy(draft)
        sent["status"] = "sent"
        sent["sent_at"] = datetime.now().isoformat()

        # -----------------------------
        # ATTACH SENDER PROFILE
        # -----------------------------
        if sender_profile:
            sent["sender_profile"] = sender_profile
        else:
            sent["sender_profile"] = {}

        # -----------------------------
        # STORE SENT EMAIL
        # -----------------------------
        self.storage.save(sent, prefix="sent")

        return {
            "status": "success",
            "message": "Email sent successfully (local send).",
            "email": sent
        }
