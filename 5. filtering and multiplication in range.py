from functools import reduce

my_list = [number for number in range(100, 1001) if number % 2 == 0]
print(reduce(lambda a, b: a * b, my_list))
