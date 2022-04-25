my_list = [7, 5, 3, 3, 2]
num = -1
while num != 0:
    num = int(input('Введите натуральное число или 0 для выхода - '))
    my_list.append(num)
    for i in range(len(my_list)):
        if my_list[i] == num:
            my_list.insert(i, num)
            my_list.pop(len(my_list) - 1)
            break
    print(my_list)