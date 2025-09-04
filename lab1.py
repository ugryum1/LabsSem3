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
            print(f"{prompt.split(':')[0]}: {sys.argv[index]}")
            return coef
        except (ValueError, IndexError):
            print(f"Некорректное значение коэффициента в командной строке.")

    # Если не получилось из командной строки, вводим с клавиатуры
    while True:
        try:
            print(prompt)
            coef_str = input()
            coef = float(coef_str)
            return coef
        except ValueError:
            print("Некорректный ввод. Попробуйте снова.")


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

    result = []
    t_roots = []

    # Решаем отностительно t = x**2
    D = b * b - 4 * a * c

    if D < 0:
        # нет корней биквадратного уравнения
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

    # Находим корни x из t = x**2
    for t in t_roots:
        if t > 0:
            x1 = math.sqrt(t)
            x2 = -math.sqrt(t)
            result.append(x1)
            result.append(x2)
        elif t == 0:
            result.append(0.0)

    return result


def main():
    '''
    Основная функция
    '''
    while True:
        a = get_coef(1, 'Введите коэффициент А:')
        if a != 0:
            break
        print("Коэффициент А не может быть равен 0 для биквадратного уравнения. Попробуйте снова.")

    b = get_coef(2, 'Введите коэффициент B:')
    c = get_coef(3, 'Введите коэффициент C:')

    # Вычисление корней
    roots = get_roots(a, b, c)

    # Вывод корней
    len_roots = len(roots)
    if len_roots == 0:
        print('Нет действительных корней')
    elif len_roots == 1:
        print('Один действительный корень: {}'.format(roots[0]))
    elif len_roots == 2:
        print('Два действительных корня: {} и {}'.format(roots[0], roots[1]))
    elif len_roots == 3:
        print('Три действительных корня: {}, {}, {}'.format(roots[0], roots[1], roots[2]))
    elif len_roots == 4:
        print('Четыре действительных корня: {}, {}, {}, {}'.format(roots[0], roots[1], roots[2], roots[3]))


# Если сценарий запущен из командной строки
if __name__ == "__main__":
    main()

# Пример запуска
# qr.py 1 0 -4