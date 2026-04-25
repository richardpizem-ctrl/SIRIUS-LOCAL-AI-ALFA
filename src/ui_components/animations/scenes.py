class BaseScene:
    """Základná scéna – všetky animácie budú z tohto dedičné."""
    def __init__(self):
        self.objects = []  # zoznam grafických objektov v scéne
        self.active = False

    def start(self):
        """Spustenie scény."""
        self.active = True

    def stop(self):
        """Zastavenie scény."""
        self.active = False

    def update(self, delta_time: float):
        """Aktualizácia scény – implementuje sa v potomkoch."""
        pass


class MoveScene(BaseScene):
    """Animácia pre presun súborov (poštár)."""
    def __init__(self):
        super().__init__()

    def update(self, delta_time: float):
        pass  # sem pôjde logika pohybu postavičky


class CopyScene(BaseScene):
    """Animácia pre kopírovanie (kopírka)."""
    def __init__(self):
        super().__init__()

    def update(self, delta_time: float):
        pass  # sem pôjde logika kopírovania


class DeleteScene(BaseScene):
    """Animácia pre mazanie (skartovačka)."""
    def __init__(self):
        super().__init__()

    def update(self, delta_time: float):
        pass  # sem pôjde logika skartovania


class CreateFolderScene(BaseScene):
    """Animácia pre vytvorenie priečinka."""
    def __init__(self):
        super().__init__()

    def update(self, delta_time: float):
        pass  # sem pôjde animácia vytvárania priečinka
