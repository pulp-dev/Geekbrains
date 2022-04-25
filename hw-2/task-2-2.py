elements = []
amount = int(input('Введите количество элементов - '))
for i in range(amount):
    elements.append(input(f'Введите {i + 1} элемент - '))
if amount % 2 != 0:
    for i in range(0, amount - 1, 2):
        a = elements[i + 1]
        elements[i + 1] = elements[i]
        elements[i] = a
    print(elements[:])
else:
    for i in range(0, amount, 2):
        a = elements[i + 1]
        elements[i + 1] = elements[i]
        elements[i] = a
    print(elements[:])