number = int(input('Введите целое положительное число '))
max_number = 0
while number > 0:
    get_number = number % 10
    if max_number < get_number:
        max_number = get_number
    number = (number - get_number) // 10
print(f'Максимальное число {max_number}')
