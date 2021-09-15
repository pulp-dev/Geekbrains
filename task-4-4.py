def is_more_then_two(el, nums_):
    not_only = [j for j in nums_ if j == el]
    amount = len(not_only)
    if amount > 1:
        return False
    else:
        return True


nums = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
new_nums = []
for i in nums:
    if is_more_then_two(i, nums):
        new_nums.append(i)
print(new_nums)