from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square

from tabulate import tabulate

def main():
    N = int(input("Введите число N: "))

    rectangle = Rectangle(N, N, "синий")
    circle = Circle(N, "зелёный")
    square = Square(N, "красный")

    print(rectangle)
    print(circle)
    print(square)

    table = [
        ["Прямоугольник", rectangle.color.color, rectangle.area()],
        ["Круг", circle.color.color, f"{circle.area():.2f}"],
        ["Квадрат", square.color.color, square.area()]
    ]

    print("\nТаблица площадей фигур:")
    print(tabulate(table, headers=["Фигура", "Цвет", "Площадь"], tablefmt="grid"))

if __name__ == "__main__":
    main()
