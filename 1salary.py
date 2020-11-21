from sys import argv

first_param, second_param, third_param = argv[1:]


def salary(first_param, second_param, third_param):
    return int(first_param) * int(second_param) + int(third_param)


try:
    print(int(salary(first_param, second_param, third_param)))

except ValueError:
    print('Введите числа')
