from itertools import count, cycle

x = int(input())
for i in count(x):
    if i == x * 100:
        break
    print(i)

data = ['f', 'r', 3, 69]
count_ = 0
for i in cycle(data):
    print(i)
    count_ += 1
    if count_ // len(data) == 2:
        break