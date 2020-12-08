def my_func(arg_1, arg_2, arg_3):
    set_1 = {arg_1, arg_2, arg_3}
    list_1 = list({arg_1, arg_2, arg_3} - {min(set_1)})
    return int(list_1[0]) + int(list_1[1])


print(my_func(arg_1=input('Введите первое число '), arg_2=input('Введите второе число '),
              arg_3=input('Введите третье число ')))
