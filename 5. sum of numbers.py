result_1 = 0


def sum_numbers(list_numbers):
    """Возвращает сумму элементов, после преобразования из str."""
    result = (int(item) for item in list_numbers)
    return sum(result)


while True:
    number_str = input('Введите числа через пробел ')
    number_list = number_str.split()
    if 'q' in number_list:
        result_1 = result_1 + int(sum_numbers(number_list[:(number_list.index('q'))]))
        print(result_1, f'({sum_numbers(number_list[:(number_list.index("q"))])})')
        break
    else:
        result_1 = result_1 + int(sum_numbers(number_list))
        print(result_1, f'({sum_numbers(number_list)})')
