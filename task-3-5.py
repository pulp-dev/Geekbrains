def sum_or_exit(nums_to_sum, final_sum):
    a = nums_to_sum.split(' ')
    print(a)
    for i in a:
        if i == '/':
            return final_sum, i
        final_sum  += int(i)
    return final_sum, None



def main():
    final_sum = 0
    i = None
    while i != '/':
        nums_to_sum = input('Введите строку чисел или "/" для выхода - ')
        final_sum, i = sum_or_exit(nums_to_sum, final_sum)
        print(final_sum)


main()