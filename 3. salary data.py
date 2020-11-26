sum_sal = 0
workers_list = []
salary_list = []
with open("text_3.txt", 'r', encoding='utf-8') as fi_1:
    words_list = sum([word.split() for word in [line.rstrip() for line in fi_1.readlines()]], [])
    for i in range(1, len(words_list), 2):
        salary_list.append(words_list[i])
        workers_list.append(words_list[i - 1])
    for name in [workers_list[b] for b in range(len(salary_list)) if float(salary_list[b]) < 20000]:
        print(name, end=' ')

    for price in salary_list:
        sum_sal += float(price)
    print(f'\n------ Средняя величина дохода: {sum_sal / len(salary_list)}')
