class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return 'Запуск отрисовки'


class Pen(Stationery):
    def __init__(self, title='pen'):
        super().__init__(title)

    def draw(self):
        return 'Запуск отрисовки ручкой'


class Pencil(Stationery):
    def __init__(self, title='pencil'):
        super().__init__(title)

    def draw(self):
        return 'Запуск отрисовки карандашом'


class Handle(Stationery):
    def __init__(self, title='handle'):
        super().__init__(title)

    def draw(self):
        return 'Запуск отрисовки маркером'


stat = Stationery('pen')
pen = Pen()
pencil = Pencil()
handle = Handle()
print(stat.draw())
print(pen.draw())
print(pencil.draw())
print(handle.draw())
