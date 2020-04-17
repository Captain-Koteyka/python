# Вариант 1, c использованием **
def my_func1(x: int, y: int) -> float:
    """
    Эта функция принимает действительное положительное число x и целое отрицательное число y
    и возводит x в степень y
    :param x: int
    :param y: int, y < 0
    :return: float, x в степени y
    """
    return x**y


# Вариант 2, с использованием цикла
def my_func2(x: int, y: int) -> float:
    """
    Эта функция принимает действительное положительное число x и целое отрицательное число y
    и возводит x в степень y
    :param x: int
    :param y: int, y < 0
    :return: float, x в степени y
    """
    y *= -1
    result = x
    for i in range(1, y):
        result *= x
    return 1 / result
