with open("my_file.txt", 'w', encoding='utf-8') as fi:
    while True:
        string_1 = input('Введите первую строку и нажмите enter. Для выхода введите пустую строку. ')
        if string_1 == '':
            break
        else:
            fi.write(f'{string_1}\n')
