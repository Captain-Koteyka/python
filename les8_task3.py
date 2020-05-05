class NotDigitError(Exception):
    def __init__(self, text):
        self.text = text


num_list = []
while True:
    try:
        data = input('Введите число\n')
        if data.isdigit():
            num_list.append(int(data))
        elif data == 'stop':
            break
        else:
            raise NotDigitError('Ошибка: введена строка')
    except NotDigitError as error:
        print(error)
print(num_list)
