nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
subjects = {}
with open('subjects.txt', 'r') as file:
    text = file.read()
    for i in text.split('\n'):
        subj = i.split(':')[0]
        sum_ = 0
        num = ''
        for j in i.split(':')[1]:
            if j in nums:
                num += j
            if j == '(':
                sum_ += int(num)
                num = ''
        subjects[subj] = sum_
print(subjects)