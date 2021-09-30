def are_arguments_str(*args):
    count = 0
    for i in args:
        if isinstance(i, str):
            count += 1
    if count == len(args):
        return True
    return False

class Storage:
    def __init__(self, name, locality, technique_in_storage={}, technique_in_departments={}):
        self.name = name
        self.locality = locality
        self.technique_in_storage = dict(technique_in_storage)
        self.technique_in_departments = dict(technique_in_departments)
        i = False
        while i:
            if are_arguments_str(self.name, self.locality):
                i = True
            else:
                print('Введите строку')


    def technique_input(self, other):
        if other.name in self.technique_in_storage:
            self.technique_in_storage[other.name] = \
                [other.amount + self.technique_in_storage[other.name][0], 'Склад']
        else:
            self.technique_in_storage[other.name] = [other.amount, 'Склад']

    def technique_output(self, other, amount, place):
        if other.name in self.technique_in_departments:
            self.technique_in_departments[other.name] = \
                [amount + self.technique_in_departments[other.name][0], place]
            self.technique_in_storage[other.name][0] -= amount
        else:
            self.technique_in_departments[other.name] = [other.amount, place]
            self.technique_in_storage[other.name][0] -= amount


class OfficeEquipment:
    def __init__(self, name, model, date_of_issue, amount):
        self.name = name
        self.model = model
        self.date_of_issue = date_of_issue
        self.amount = amount
        i = False
        while i:
            if are_arguments_str(self.name, self.model, self.date_of_issue):
                i = True
            else:
                print('Введите строку')


class Printer(OfficeEquipment):
    paper_value = 100


class Xerox(OfficeEquipment):
    internet_connection = True


class Phone(OfficeEquipment):
    number = '12-34-56'

