num = int(input())
i = 10
res = num // i
while res != 0:
    i = i * 10
    res = num // i
i = i / 10
max_ = num % 10
a = 10
while a <= i:
    res = num // a % 10
    if  res > max_:
        max_ = res
    a = a * 10
print(max_)