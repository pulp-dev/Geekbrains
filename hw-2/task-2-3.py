months ={'зима': [12, 1, 2], 'весна': [3, 4, 5], 'лето': [6, 7, 8], 'осень': [9, 10, 11]}
seasons = ('зима', 'весна', 'лето', 'осень')

month_num = int(input())

for i in seasons:
    if month_num in months[i]:
        print(i)
