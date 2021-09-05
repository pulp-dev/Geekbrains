print('proceeds')
proceeds = int(input())
print('costs')
costs = int(input())
if proceeds < costs:
    print('not stonks 🗿')
else:
    print('stonks 👍')
    print('рентабельность выручки:', "%.1f" % ((proceeds - costs) / proceeds))
    print('численность сотрудников')
    workers = int(input())
    print('прибыль фирмы в расчете на одного сотрудника:', "%.2f" % ((proceeds - costs) / workers))