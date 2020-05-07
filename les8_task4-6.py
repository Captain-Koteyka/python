class NotDigitError(Exception):
    def __init__(self, text):
        self.text = text


class Warehouse:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    @staticmethod
    def reception():
        warehouse_dict = {}
        while True:
            name = input('Введите наименование или stop для окончания ввода\n')
            if name == 'stop':
                break
            try:
                price = input('Введите цену или stop для окончания ввода\n')
                if price.isdigit():
                    price = int(price)
                elif price == 'stop':
                    break
                else:
                    raise NotDigitError('Ошибка: введена строка\n')
            except NotDigitError as error:
                print(error)
                continue
            quantity = input('Введите количество или stop для окончания ввода\n')
            try:
                if quantity.isdigit():
                    quantity = int(quantity)
                    warehouse_dict[name] = price, quantity
                elif quantity == 'stop':
                    break
                else:
                    raise NotDigitError('Ошибка: введена строка\n')
            except NotDigitError as error:
                print(error)
        return warehouse_dict

    @staticmethod
    def transfer(reception: dict):
        transfer_dict = {}
        while True:
            k = input('Введите название предмета для перемещения со склада или stop для окончания ввода\n')
            if k == 'stop':
                break
            else:
                transfer_dict[k] = reception[k]
                del reception[k]
        return transfer_dict


class OfficeEquipment:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity


class Printer(OfficeEquipment):
    def __init__(self, max_format, name, price, quantity):
        self.copy_speed = max_format
        super().__init__(name, price, quantity)


class Scanner(OfficeEquipment):
    def __init__(self, optical_resolution, name, price, quantity):
        self.copy_speed = optical_resolution
        super().__init__(name, price, quantity)


class Copier(OfficeEquipment):
    def __init__(self, copy_speed, name, price, quantity):
        self.copy_speed = copy_speed
        super().__init__(name, price, quantity)


equipment = Warehouse.reception()
print(Warehouse.transfer(equipment))
print(equipment)
