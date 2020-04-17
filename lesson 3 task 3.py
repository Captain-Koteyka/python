def my_func(var_1: float, var_2: float, var_3: float) -> float:
    """
    Это функция, которая принимает три аргумента, и возвращает сумму наибольших двух аргументов.
    :param var_1: float
    :param var_2: float
    :param var_3: float
    :return: float результат вычислений
    """
    if var_1 < var_2 and var_1 < var_3:
        return var_2 + var_3
    elif var_2 < var_1 and var_2 < var_3:
        return var_1 + var_3
    elif var_3 < var_1 and var_3 < var_2:
        return var_1 + var_2
