class IsItANumber(Exception):
    def __init__(self, text):
        self.text = text


def append_smth(data, i):
    try:
        data.append(int(i))
    except:
        raise IsItANumber('Введите число >:|')
    return data


data = []

i = input()
while i != 'stop':
    try:
        data = append_smth(data, i)
    except IsItANumber:
        print('Введите число >:|')
    i = input()

print(data)