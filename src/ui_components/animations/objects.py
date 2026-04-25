from dataclasses import dataclass

@dataclass
class DrawableObject:
    """Základný grafický objekt – všetky tvary budú z tohto dedičné."""
    x: float
    y: float
    color: tuple
    visible: bool = True

    def draw(self):
        """Metóda na vykreslenie objektu – implementuje sa v potomkoch."""
        pass


class Circle(DrawableObject):
    def __init__(self, x, y, radius, color):
        super().__init__(x, y, color)
        self.radius = radius

    def draw(self):
        pass  # sem pôjde DearPyGUI draw_circle


class Rectangle(DrawableObject):
    def __init__(self, x, y, width, height, color):
        super().__init__(x, y, color)
        self.width = width
        self.height = height

    def draw(self):
        pass  # sem pôjde DearPyGUI draw_rectangle


class Line(DrawableObject):
    def __init__(self, x, y, x2, y2, color):
        super().__init__(x, y, color)
        self.x2 = x2
        self.y2 = y2

    def draw(self):
        pass  # sem pôjde DearPyGUI draw_line
