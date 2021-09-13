def div(a, b):
    if b == 0:
        return 'ø'
    result = a / b
    return result


print(div(int(input()), int(input())))