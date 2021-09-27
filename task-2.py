class Clothes:
    def __init__(self, name):
        self.name = name

    def expenditure_formula(self):
        pass


class Coat(Clothes):
    def __init__(self, name, v):
        self.name = name
        self.v = v

    @property
    def expenditure_formula(self):
        return self.v / 6.5 + 0.5


class Suit(Clothes):
    def __init__(self, name, h):
        self.name = name
        self.h = h

    @property
    def expenditure_formula(self):
        return 2 * self.h + 0.3


coat = Coat('Пальто Burberry', 44)
suit = Suit('Костьюм Hugo Boss', 45)
print(round(coat.expenditure_formula, 2), suit.expenditure_formula)
