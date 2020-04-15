name1 = input('Введите название товара №1\n')
while True:
    price1 = input('Введите цену товара №1\n')
    if price1.isdigit():
        price1 = int(price1)
        break
    else:
        print('Ошибка ввода, введите только число\n')
while True:
    number1 = input('Введите количество товара №1\n')
    if number1.isdigit():
        number1 = int(number1)
        break
    else:
        print('Ошибка ввода, введите только число\n')
unit1 = input('Введите единицы измерения товара №1\n')
name2 = input('Введите название товара №2\n')
while True:
    price2 = input('Введите цену товара №2\n')
    if price2.isdigit():
        price2 = int(price2)
        break
    else:
        print('Ошибка ввода, введите только число\n')
while True:
    number2 = input('Введите количество товара №2\n')
    if number2.isdigit():
        number2 = int(number2)
        break
    else:
        print('Ошибка ввода, введите только число\n')
unit2 = input('Введите единицы измерения товара №2\n')
name3 = input('Введите название товара №3\n')
while True:
    price3 = input('Введите цену товара №3\n')
    if price3.isdigit():
        price3 = int(price3)
        break
    else:
        print('Ошибка ввода, введите только число\n')
while True:
    number3 = input('Введите количество товара №3\n')
    if number3.isdigit():
        number3 = int(number3)
        break
    else:
        print('Ошибка ввода, введите только число\n')
unit3 = input('Введите единицы измерения товара №3\n')

goods = [
    (1, {'название': name1, 'цена': price1, 'количество': number1, 'ед': unit1}),
    (2, {'название': name2, 'цена': price2, 'количество': number2, 'ед': unit2}),
    (3, {'название': name3, 'цена': price3, 'количество': number3, 'ед': unit3})
]
print(goods)
goods_dict = {}
name = []
price = []
number = []
unit = []
for itm in goods:
    name.append(itm[1]['название'])
    price.append(itm[1]['цена'])
    number.append(itm[1]['количество'])
    unit.append(itm[1]['ед'])
goods_dict['название'] = name
goods_dict['цена'] = price
goods_dict['количество'] = number
goods_dict['ед'] = unit
print(goods_dict)
