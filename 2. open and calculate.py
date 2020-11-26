with open("my_file.txt", 'r+', encoding='utf-8') as fi_1:
    while True:
        string_1 = input('Введите первую строку и нажмите enter. Для выхода введите пустую строку. ')
        if string_1 == '':
            break
        else:
            fi_1.write(f'{string_1}\n')
with open("my_file.txt", 'r+', encoding='utf-8') as fi_1:
    string_list = fi_1.readlines()
    print(f'Количество строк в файле: {len(string_list) + 1}')
    a = 1
    for word in string_list:
        print(f"Количество слов в {a} строке:{len(word.split())}")
        a += 1
    print(f"Количество слов в {a} строке:0")
