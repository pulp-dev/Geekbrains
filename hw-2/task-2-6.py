goods = []
answer = ''
count = 1
while answer != '0':
    print('Введите название товара или 0 для выхода')
    answer = input()
    if answer == '0':
        break
    name = answer
    print('Введите цену товара')
    answer = int(input())
    cost = answer
    print('Введите количество товара')
    answer = int(input())
    amount = answer
    print('Введите единицу измерения товара')
    answer = input()
    messure = answer
    goods.append((count, {'название':name, 'цена':cost, 'количество':amount, 'eд':messure}))
    count += 1
analytics = {'название':[], 'цена':[], 'количество':[], 'eд':[]}
list_ = []
i = 0
while i < len(goods):
    analytics['название'].append(goods[i][1]['название'])
    analytics['цена'].append(goods[i][1]['цена'])
    analytics['количество'].append(goods[i][1]['количество'])
    analytics['eд'].append(goods[i][1]['eд'])
    i += 1
print(analytics)