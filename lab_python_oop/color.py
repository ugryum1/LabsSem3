class FigureColor:
    def __init__(self, color = "бесцветный"):
        self._color = color

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, new_color: str):
        self._color = new_color

    def __repr__(self):
        return f"{self._color}"
