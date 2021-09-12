def my_func(a, b, c):
    args = [a, b, c]
    max_ = a
    min_ = a
    for i in args:
        if i > max_:
            max_ = i
        if i < min_:
            min_ = i
    for i in args:
        if (i < max_) and (i > min_):
            return max_ + i


print(my_func(int(input()), int(input()), int(input())))