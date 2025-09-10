from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square

def main():
    N = int(input("Введите число N: "))

    rectangle = Rectangle(N, N, "синий")
    circle = Circle(N, "зелёный")
    square = Square(N, "красный")

    print(rectangle)
    print(circle)
    print(square)

if __name__ == "__main__":
    main()
