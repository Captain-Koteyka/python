class Warehouse:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    @staticmethod
    def reception(self):
        reception_dict = {}
        try:
            name = input('Введите название')
            price = input('Введите цену')
        reception_dict[self.name] = self.price
        return reception_dict

    def transfer(self):
        pass


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


printer = Printer('A4', 'fff', 654, 15)
print(printer.reception)
