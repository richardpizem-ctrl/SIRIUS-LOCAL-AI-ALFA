import re


class EmailValidator:
    """
    EmailValidator 4.0
    Provides validation utilities for email addresses, subjects,
    body text, and attachment paths.

    This module is used internally by EmailManager and commands.
    """

    # ---------------------------------------------------------
    # EMAIL ADDRESS VALIDATION
    # ---------------------------------------------------------
    EMAIL_REGEX = re.compile(
        r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
    )

    def validate_email(self, email: str) -> bool:
        """
        Validates an email address format.
        """
        if not isinstance(email, str):
            return False
        return bool(self.EMAIL_REGEX.match(email))

    # ---------------------------------------------------------
    # SUBJECT VALIDATION
    # ---------------------------------------------------------
    def validate_subject(self, subject: str) -> bool:
        """
        Validates subject length and type.
        """
        if not isinstance(subject, str):
            return False
        if len(subject.strip()) == 0:
            return False
        if len(subject) > 300:
            return False
        return True

    # ---------------------------------------------------------
    # BODY VALIDATION
    # ---------------------------------------------------------
    def validate_body(self, body: str) -> bool:
        """
        Validates email body text.
        """
        if not isinstance(body, str):
            return False
        if len(body.strip()) == 0:
            return False
        return True

    # ---------------------------------------------------------
    # ATTACHMENT VALIDATION
    # ---------------------------------------------------------
    def validate_attachment(self, path: str) -> bool:
        """
        Validates attachment path format.
        (File existence is checked elsewhere.)
        """
        if not isinstance(path, str):
            return False
        if len(path.strip()) == 0:
            return False
        return True

    # ---------------------------------------------------------
    # FULL EMAIL VALIDATION
    # ---------------------------------------------------------
    def validate_full(self, to: str, subject: str, body: str) -> dict:
        """
        Validates all components of an email.
        Returns a dict with validation results.
        """
        return {
            "email_valid": self.validate_email(to),
            "subject_valid": self.validate_subject(subject),
            "body_valid": self.validate_body(body),
            "all_valid": (
                self.validate_email(to)
                and self.validate_subject(subject)
                and self.validate_body(body)
            )
        }
