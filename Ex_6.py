a = int(input(f'Введите начальный результат '))
b = int(input(f'Введите цель '))
days = 0
while a < b:
    days += 1
    a = a + a/10
    print(f'{days}-й день, {a:.2f}')
print(f'Вам понадобится {days} дней ')
