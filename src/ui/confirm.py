class ConfirmDialog:
    """
    Mock UI Confirm Dialog
    Dočasná verzia – vždy vráti True.
    Neskôr sa nahradí reálnym UI oknom.
    """

    def __init__(self, title: str, message: str):
        self.title = title
        self.message = message

    def get_user_confirmation(self) -> bool:
        """
        Dočasne automaticky potvrdí operáciu.
        """
        return True
