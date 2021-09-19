def get_a_dict_from_file():
    slaves ={}
    with open('slaves.txt', 'r') as file:
        data = file.read().split('\n')
        for i in data:
            slaves[i.split()[0]] = int(i.split()[1])
    return slaves


def average_salary(slaves):
    sum_ = 0
    for i in slaves:
        sum_ += slaves[i]
    return sum_ / len(slaves)


low_cost_slaves = []
slaves = get_a_dict_from_file()
for i in slaves:
    if slaves[i] < 20000:
        low_cost_slaves.append(i)
print(low_cost_slaves)
print(f"Средняя зарплата {'%.2f' % (average_salary(slaves))}")