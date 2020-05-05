class MyZeroDivisionError(Exception):
    def __init__(self, text):
        self.text = text


while True:
    try:
        numbers = list(map(int, input('Введите два числа: делимое и делитель\n').split()))
        if numbers[1] == 0:
            raise MyZeroDivisionError('Деление на ноль невозможно')
    except MyZeroDivisionError as error:
        print(error)
    else:
        print(numbers[0] / numbers[1])
        break
