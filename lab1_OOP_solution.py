import sys
import math

class BiquadraticSolver:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def solve(self):
        a, b, c = self.a, self.b, self.c

        # Списки для итоговых корней и корней t = x**2, соответственно
        result = []
        t_roots = []

        # Решаем отностительно t = x**2
        D = b * b - 4 * a * c

        if D < 0:
            # Нет корней биквадратного уравнения
            return result

        if D == 0.0:
            t = -b / (2.0 * a)
            t_roots.append(t)
        elif D > 0.0:
            sqD = math.sqrt(D)
            t1 = (-b + sqD) / (2.0 * a)
            t2 = (-b - sqD) / (2.0 * a)
            t_roots.append(t1)
            t_roots.append(t2)
        # Случай с отрицательным D нет смысла обрабатывать, нет корней

        # Находим корни x из t = x**2
        for t in t_roots:
            if t > 0:
                x_abs = math.sqrt(t)
                result.extend([x_abs, -x_abs])
            elif t == 0:
                result.append(0.0)

        result = [round(i, 2) for i in result]
        return result

    def print_solution(self):
        roots = self.solve()

        # Вывод корней
        len_roots = len(roots)
        if len_roots == 0:
            print("Нет действительных корней")
        elif len_roots == 1:
            print("Один действительный корень: {}".format(roots[0]))
        elif len_roots == 2:
            print("Два действительных корня: {} и {}".format(roots[0], roots[1]))
        elif len_roots == 3:
            print("Три действительных корня: {}, {}, {}".format(roots[0], roots[1], roots[2]))
        elif len_roots == 4:
            print("Четыре действительных корня: {}, {}, {}, {}".format(roots[0], roots[1], roots[2], roots[3]))


class InputHandler:
    @staticmethod
    def get_coef(index, prompt):
        if index < len(sys.argv):
            try:
                coef = float(sys.argv[index])
                print(f"{prompt.split(':')[0]}: {sys.argv[index]}")
                return coef
            except (ValueError, IndexError):
                print("Некорректное значение коэффициента в командной строке.")

        # Если не получилось из командной строки, вводим с клавиатуры
        while True:
            try:
                print(prompt)
                coef_str = input()
                coef = float(coef_str)
                return coef
            except ValueError:
                print("Некорректный ввод, попробуйте снова.")


def main():
    while True:
        a = InputHandler.get_coef(1, "Введите коэффициент А:")
        if a != 0:
            break
        print("Коэффициент А не может быть равен 0 для биквадратного уравнения. Введите снова.")

    b = InputHandler.get_coef(2, "Введите коэффициент B:")
    c = InputHandler.get_coef(3, "Введите коэффициент C:")

    solver = BiquadraticSolver(a, b, c)
    solver.print_solution()

# Если сценарий запущен из командной строки
if __name__ == "__main__":
    main()
