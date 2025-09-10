from lab_python_oop.geom_figure import GeomFigure
from lab_python_oop.color import FigureColor

class Rectangle(GeomFigure):
    name = "прямоугольник"

    def __init__(self, width, height, color: str):
        self.width = width
        self.height = height
        self.color = FigureColor(color)

    def area(self):
        return self.height * self.width

    def __repr__(self):
        return "Фигура: {0}, ширина: {1}, высота: {2}, цвет: {3}, площадь: {4}".format(
            self.get_name(),
            self.width,
            self.height,
            self.color.color,
            str(self.area())
        )
