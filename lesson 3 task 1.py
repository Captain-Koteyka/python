def division():
    while True:
        while True:
            a = input()
            b = input()
            if a.isdigit() and b.isdigit():
                a = int(a)
                b = int(b)
                break
            else:
                print('Ошибка ввода, введите только число\n')
        if b != 0:
            return a / b
            break
        else:
            try:
                a / b
            except ZeroDivisionError:
                print('Деление на ноль невозможно')
            finally:
                print('Введите делитель, отличный от нуля')


n = division()
print(n)
