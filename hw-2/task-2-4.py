words = input('Введите строку - ').split()
for i in range(len(words)):
    print(i + 1, ') ', words[i][:10], sep='')