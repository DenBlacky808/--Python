while True:
    winter = [12, 1, 2]
    spring = [3, 4, 5]
    summer = [6, 7, 8]
    autumn = [9, 10, 11]
    month = int(input('Input number of month '))
    if 0 < month < 13:
        if month in winter:
            print('winter')
        elif month in spring:
            print('Spring!')
        elif month in summer:
            print('Summer!')
        else:
            print('autumn..')
        break
    else:
        print('Please input number of month ')
