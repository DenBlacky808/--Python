name = 'Кристина'
age = 35

print(f"Привет! Ты же {name}?")
otvet = input('да/нет ')
if otvet == 'да':
    print('Приятно познакомиться! Я Денис :)')
else:
    name = input('Ой, поначалу сложно запомнить все имена. А как тебя зовут? ')
    print(f'Тогда будем знакомы {name}! Я Денис :)')
otvet_2 = input(f'Дай-ка я угадаю.. Тебе явно меньше {age} лет? Хотя ты можешь и не говорить сколько тебе лет. ')
if otvet_2 != '':
    if int(otvet_2) < 35:
        print('Я так и знал!')
    else:
        print('Но выглядишь явно моложе! ;)')
else:
    print('Понимаю, нескромный вопрос.')
print(f'Ладно, мне пора делать другие задания! Рад знакомству {name}!')