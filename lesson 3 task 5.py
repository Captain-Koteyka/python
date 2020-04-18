def sum_of_numbers(*args) -> int:
    """
    Функция суммирует введенные пользователем числа.
    После введения символа * функция прекращает работу
    :param args: tuple
    :return: int, сумма всех введенных чисел
    """
    result = 0
    while True:
        my_tuple = input()
        if '*' in my_tuple:
            if len(my_tuple) == 1:
                break
            else:
                my_tuple = my_tuple[:-1]
                my_tuple = tuple(map(int, my_tuple.split()))
                result += sum(my_tuple)
                break
        else:
            my_tuple = tuple(map(int, my_tuple.split()))
            result += sum(my_tuple)
            print(result)
    return result


some_var = sum_of_numbers()
print(some_var)
