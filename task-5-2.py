def lines_and_words_counter(text):
    lines_num = len(text)
    words_num = 0
    for i in text:
        words_num += len(i.split())
    return lines_num, words_num


with open('lines_and_words_to_count.txt', 'r') as file:
    text = file.read().split('\n')
    print(lines_and_words_counter(text))