import random

with open("my_file_2.txt", 'w', encoding='utf-8') as fi:
    fi.writelines([f'{random.randint(1, 100)} ' for _ in range(1, 10)])
with open("my_file_2.txt", 'r', encoding='utf-8') as fi:
    print(f'Сумма чисел равна: {sum(map(int, fi.readlines()[0].split()))}')
