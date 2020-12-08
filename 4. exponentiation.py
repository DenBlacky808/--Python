def exp_xy(x, y):
    try:
        x_tmp = x
        for i in range(1, abs(y)):
            x = x * x_tmp
        return 1 / x
    except ZeroDivisionError:
        print('Ноль не может быть в отрицательной степени.')


while True:
    try:
        x_1 = int(input('Введите x - положительное число! '))
        y_1 = int(input('Введите y - целое отрицательное число! '))
        y_2 = str(abs(y_1))
        if x_1 > 0 and y_1 < 0 and '.' not in y_2:
            print(exp_xy(x_1, y_1))
            break
        else:
            raise ValueError
    except ValueError:
        print('Необходимо вводить числа корректно!')
