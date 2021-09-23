class Worker:

    income_ = {"wage": 20000, "bonus": 4500}

    def __init__(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = position


class Position(Worker):

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return self.income_['wage'] + self.income_['bonus']


worker = Position('Mihail', 'Zubenko', "Vor v zakone")
print(worker.get_full_name(), worker.get_total_income())