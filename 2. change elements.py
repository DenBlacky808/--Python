index_1 = 0
index_2 = 0
while True:
    list_len = int(input('How many elements will be in your list? '))
    if list_len > 0:
        elements_1 = []
        elements_2 = []
        for index_1 in range(list_len):
            elements_1.append(input('Please input element of list '))
        for index_2 in range(0, index_1, 2):
            elements_2.append(elements_1[index_2 + 1])
            elements_2.append(elements_1[index_2])
        if index_1 % 2 == 0:
            elements_2.append(elements_1[index_2 + 2])
        print(elements_2)
        break
    else:
        print('Please input number of elements > 0')
