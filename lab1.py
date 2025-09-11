import sys
import math


def get_coef(index, prompt):
    '''
    Читаем коэффициент из командной строки или вводим с клавиатуры

    Args:
        index (int): Номер параметра в командной строке
        prompt (str): Приглашение для ввода коэффицента

    Returns:
        float: Коэффициент квадратного уравнения
    '''

    # Сначала пробуем получить из командной строки
    if index < len(sys.argv):
        try:
            coef = float(sys.argv[index])
            if index == 1 and coef == 0.0:
                print("Коэффициент А не может быть равен 0 для биквадратного уравнения. Введите снова.")
            else:
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
            if index == 1 and coef == 0.0:
                print("Коэффициент А не может быть равен 0 для биквадратного уравнения. Введите снова.")
                continue
            return coef
        except ValueError:
            print("Некорректный ввод, попробуйте снова.")


def get_roots(a, b, c):
    '''
    Вычисление корней квадратного уравнения

    Args:
        a (float): коэффициент А
        b (float): коэффициент B
        c (float): коэффициент C

    Returns:
        list[float]: Список корней
    '''

    # Списки для итоговых корней и корней t = x**2, соответственно
    result = []
    t_roots = []

    # Решаем отностительно t = x**2
    D = b * b - 4 * a * c

    if D < 0:
        # Нет корней биквадратного уравнения
        return  result

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

def print_equation(a, b, c):
    # Вывод уравнения на экран
    a = int(a) if a == int(a) else a
    b = int(b) if b == int(b) else b
    c = int(c) if c == int(c) else c

    print("\nУравнение: ")

    summand1 = ("" if a >= 0 else "-") + (str(abs(a)) if abs(a) != 1 else "") + "x**4"
    summand2 = ((" + " if b > 0 else " - ") + (str(abs(b)) if abs(b) != 1 else "") + "x**2") if b else ""
    summand3 = ((" + " if c > 0 else " - ") + str(abs(c))) if c else ""
    equation = summand1 + summand2 + summand3 + " = 0"

    print(equation + "\n")

def main():
    '''
    Основная функция
    '''
    while True:
        a = get_coef(1, "Введите коэффициент А:")
        if a != 0:
            break
        print("Коэффициент А не может быть равен 0 для биквадратного уравнения. Введите снова.")

    b = get_coef(2, "Введите коэффициент B:")
    c = get_coef(3, "Введите коэффициент C:")

    # Вычисление корней
    roots = get_roots(a, b, c)

    # Вывод уравнения
    print_equation(a, b, c)

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


# Если сценарий запущен из командной строки
if __name__ == "__main__":
    main()
