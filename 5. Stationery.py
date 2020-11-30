class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return print(f'Запуск отрисовки.')


class Pen(Stationery):
    def draw(self):
        return print(f'Запуск отрисовки при помощи {self.title}')


class Pencil(Stationery):
    def draw(self):
        return print(f'Рисуем используя {self.title}')


class Handle(Stationery):
    def draw(self):
        return print(f'Взяли в руки {self.title} для отрисовки')


pen_1 = Pen('Ручки')
pencil_1 = Pencil('Карандаш')
marker_1 = Handle('Маркер')
pen_1.draw()
pencil_1.draw()
marker_1.draw()
