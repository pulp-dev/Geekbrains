class ComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.num = f'{a} + {b}j'

    def __str__(self):
        return self.num

    def __add__(self, other):
        return f'{self.a + other.a} + {self.b + other.b}j'

    def __mul__(self, other):
        return f'{self.a * other.a - (self.b * other.b)} + {self.b * other.a}j'


a = ComplexNumber(1, 1)
b = ComplexNumber(2, 2)
print(a)
print(a + b)
print(a * b)