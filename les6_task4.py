from random import choice


class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'Автомобиль {self.name} начал движение со скоростью {self.speed} км/ч'

    def stop(self):
        return f'Автомобиль {self.name} остановился'

    def turn(self, direction=choice(('налево', 'направо'))):
        return f'Автомобиль {self.name} повернул {direction}'

    def show_speed(self):
        return f'Скорость автомобиля {self.name} составляет {self.speed} км/ч'


class TownCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(self, speed, color, name)
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = False

    def show_speed(self):
        if self.speed > 60:
            return f'Автомобиль {self.name} двигается с превышением скорости'
        else:
            return f'Скорость автомобиля {self.name} составляет {self.speed} км/ч'


class SportCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(self, speed, color, name)
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = False


class WorkCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(self, speed, color, name)
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = False

    def show_speed(self):
        if self.speed > 40:
            return f'Автомобиль {self.name} двигается с превышением скорости'
        else:
            return f'Скорость автомобиля {self.name} составляет {self.speed} км/ч'


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(self, speed, color, name)
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = True


car1 = WorkCar(50, 'yellow', 'Audi')
car2 = PoliceCar(100, 'white', 'BMW')
car3 = TownCar(60, 'blue', 'Mercedes')
car4 = SportCar(150, 'black', 'Porsche')
print(car3.show_speed())
print(car4.is_police)
print(car2.is_police)
print(car2.go())
print(car1.turn('налево'))
print(car2.turn())
print(car1.show_speed())
print(car3.show_speed())
print(car4.stop())
