from lab_python_oop.geom_figure import GeomFigure
from lab_python_oop.color import FigureColor

from math import pi

class Circle(GeomFigure):
    name = "круг"

    def __init__(self, radius, color: str):
        self.radius = radius
        self.color = FigureColor(color)

    def area(self):
        return pi * self.radius**2

    def __repr__(self):
        return "Фигура: {0}, радиус: {1}, цвет: {2}, площадь: {3}".format(
            self.get_name(),
            self.radius,
            self.color.color,
            str(self.area().__round__(2))
        )
