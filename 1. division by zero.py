def div_zero(num_1, num_2):
    try:
        return num_1 / num_2
    except ZeroDivisionError:
        print('На ноль делить нельзя!')


while True:
    try:
        number_1 = int(input('Введите делимое. '))
        number_2 = int(input('Введите делитель. '))
        result = div_zero(number_1, number_2)
        if result is not None:
            print(round(result, 2))
        break
    except ValueError:
        print('Надо ввести число!')
