while True:
    seasons_dict = {12: 'winter', 1: 'winter', 2: 'winter',
                    3: 'spring', 4: 'spring', 5: 'spring',
                    6: 'summer', 7: 'summer', 8: 'summer',
                    9: 'autumn', 10: 'autumn', 11: 'autumn'}

    month = int(input('Input number of month '))
    if 0 < month < 13:
        print(seasons_dict[month])
        break
    else:
        print('Please input number of month ')
