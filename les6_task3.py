class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def __init__(self, *args):
        super().__init__(*args)

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']


position1 = Position('Vasya', 'Petrov', 'engineer', 60000, 40000)
position2 = Position('Dmitry', 'Smirnov', 'geologist', 80000, 30000)
print(position1.get_full_name())
print(position1.get_total_income())
print(position2.get_full_name())
print(position2.get_total_income())
