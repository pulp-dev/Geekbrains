def int_func(string):
    a = list(string)
    new_string = ''
    index = -5
    for i in range(len(a)):
        if a[i] == ' ':
            index = i
        else:
            if i == index + 1 or i == 0:
                a[i]  = a[i].upper()
        new_string = new_string + a[i]
    return new_string


print(int_func(input('Введите строку ')))
