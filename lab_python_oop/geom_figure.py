from abc import ABC, abstractmethod

class GeomFigure(ABC):
    # Абстрактный класс для геометрических фигур

    name = "Геометрическая фигура"

    def __init__(self, color: str):
        self.color = color

    @abstractmethod
    def area(self):
        pass

    def get_name(self):
        return self.name
