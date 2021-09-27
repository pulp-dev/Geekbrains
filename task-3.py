class Check:
    def __init__(self, amount):
        if not isinstance(amount, int):
            print('Не целое число клеток')
            return
        self.amount = amount

    def __add__(self, other):
        new_check = Check(self.amount + other.amount)
        return new_check

    def __sub__(self, other):
        if self.amount - other.amount < 0:
            print('Разность < 0')
            return
        new_check= Check(self.amount - other.amount)
        return new_check

    def __mul__(self, other):
        new_check = Check(self.amount * other.amount)
        return new_check

    def __truediv__(self, other):
        new_check = Check(int(round(self.amount / other.amount, 0)))
        return new_check

    def make_order(self, num_of_cells):
        for i in range(0, self.amount, num_of_cells):
            if i + num_of_cells <= self.amount:
                for _ in range(num_of_cells):
                    print('*', end='')
                print()
            else:
                for _ in range(self.amount - i):
                    print('*', end='')
                print()


check_1 = Check(12)
check_1.make_order(5)
check_2 = Check(10)
sell_1 = check_2 + check_1
print(sell_1.amount)
sell_1 = check_2 - check_1
print(sell_1)
sell_1 = check_1 - check_2
print(sell_1.amount)
sell_1 = check_2 * check_1
print(sell_1.amount)
sell_1 = check_1 / check_2
print(sell_1.amount)
