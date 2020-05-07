class Date:
    def __init__(self, date: str):
        self.date = date

    # преобразование к списку из трех чисел
    @classmethod
    def date_to_num1(cls, date):
        num = list(map(int, date.split('-')))
        return num

    # преобразование к одному числу
    @classmethod
    def date_to_num2(cls, date):
        num = int(''.join(x for x in date if x.isdigit()))
        return num

    @staticmethod
    def validation(date: str):
        date_list = list(map(int, date.split('-')))
        day = date_list[0]
        month = date_list[1]
        year = date_list[2]
        if month > 12:
            print('Введите номер месяца: от 1 до 12')
        if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
            if day > 31:
                print('Количество дней в месяце не должно превышать 31')
        elif month == 4 or month == 6 or month == 9 or month == 11:
            if day > 30:
                print('Количество дней в месяце не должно превышать 30')
        elif month == 2:
            if day > 28:
                print('Количество дней в месяце не должно превышать 28')
        if year < 1950 or year > 2050:
            print('Введите год от 1950-го до 2050-го')


print(Date.date_to_num1('05-05-2020'))
print(Date.date_to_num2('05-05-2020'))
Date.validation('31-02-2020')
Date.validation('20-02-2060')
Date.validation('31-06-2020')
Date.validation('32-05-2020')
Date.validation('32-18-2020')
