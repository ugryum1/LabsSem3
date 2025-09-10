from lab_python_oop.color import FigureColor
from lab_python_oop.rectangle import Rectangle

class Square(Rectangle):
    name = "квадрат"

    def __init__(self, side, color: str):
        super().__init__(side, side, color) # Вызов конструктора базового класса
        self.side = side

    def area(self):
        return self.side ** 2

    def __repr__(self):
        return "Фигура: {0}, строна: {1}, цвет: {2}, площадь: {3}".format(
            self.get_name(),
            self.side,
            self.color.color,
            str(self.area())
        )
