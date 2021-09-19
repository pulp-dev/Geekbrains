with open('file_with_some_words.txt', 'x') as file:
    string = input()
    while string != '':
        file.write(string)
        file.write('\n')
        string = input()