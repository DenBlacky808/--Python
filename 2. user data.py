def user_data(name, surname, birthday, city, email, phone):
    print(f'{name} {surname} {birthday} {city} {email} {phone}')


user_data(name=input('Введите имя '), surname=input('Фамилию '), birthday=input('День рождения '),
          city=input('Город '), email=input('Электронную почту '), phone=input('Телефонный номер '))
