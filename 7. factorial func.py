while True:
    def generator(n_1):
        n_2 = 1
        for n_1 in range(1, n_1):
            n_2 *= n_1
            yield n_2


    try:
        n = int(input('Введите число N для расчета факториала '))
        if n >= 0:
            if n == 0:
                print('Факториал 0 равен 1')
                break
            for n in generator(n + 1):
                print(n)
            break
        else:
            print('Необходимо ввести число >= 0 ')
    except ValueError:
        print('Необходимо ввести число')
