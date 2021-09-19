import json


profits = {}
average = {}
with open('firms.txt', 'r') as file:
    text = file.read()
    for i in text.split('\n'):
        line = i.split()
        profits[line[0]] = int(line[2]) - int(line[3])
    sum_ = 0
    count = 0
    for i in profits:
        if profits[i] > 0:
            sum_ += profits[i]
            count += 1
    average["average_profit"] = "%.2f" % (sum_ / count)

list_to_print = [profits, average]

with open('result.json', 'x') as file:
    list_to_print = json.dump(list_to_print, file)