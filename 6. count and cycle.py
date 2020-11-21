from itertools import cycle, count

# noinspection PyBroadException
try:
    start = int(input('Введите число для итератора. '))

    for count_1 in count(start):
        print(count_1)
        if count_1 > 5 * start:
            raise Exception
except ValueError:
    print('Это должно быть число!')
except Exception:
    print('Достигли верхней границы')
# noinspection PyBroadException
try:
    elements = ['a', 'b', 'c']
    count_1 = 0
    for element in cycle(elements):
        print(element)
        count_1 += 1
        if count_1 > 5:
            raise Exception
except ValueError:
    pass
except Exception:
    print('Пора остановиться')
