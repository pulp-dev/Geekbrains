class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print(self.title + ' пишет')


class Pencil(Stationery):
    def draw(self):
        print(self.title + ' чертит')


class Handle(Stationery):
    def draw(self):
        print(self.title + ' выделяет')

pen = Pen('ручка')
pencil = Pencil('карандаш')
handle = Handle('маркер')
stationers = [pen, pencil, handle]
for i in stationers:
    i.draw()
