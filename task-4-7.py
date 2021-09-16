def fact(n):
    fac = 1
    for i in range(1, n + 1):
        fac = fac * i
        yield fac


for el in fact(int(input())):
    print(el)