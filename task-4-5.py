from functools import reduce

nums_to_multiply = [i for i in range(100, 1001) if i % 2 == 0]
print(reduce(lambda a, b: a * b, nums_to_multiply))