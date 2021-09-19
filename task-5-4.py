english_and_russian_counters = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}

def changer(file):
    text = ''
    for i in file.read().split('\n'):
        for j in english_and_russian_counters:
            if j in i:
                text += english_and_russian_counters[j] + '-' + i[len(i) - 1] + '\n'
    return text


with open('counters.txt', 'r') as file:
    text = changer(file)

with open('counters_in_russian.txt', 'x') as file:
    file.write(text)