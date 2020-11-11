a = int(input(f'Введите начальный результат '))
b = int(input(f'Введите цель '))
days = 1
while a < b:
    a = a + a/10
    print(f'{days}-й день, {a:.2f}')
    days += 1
print(f'Вам понадобится {days} дней ')
