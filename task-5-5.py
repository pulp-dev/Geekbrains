from random import randrange

with open('nums_to_sum.txt', 'x') as file:
    count = 0
    for i in range(10):
        a = randrange(10000)
        count += a
        file.write(str(a) + ' ')
print(count)