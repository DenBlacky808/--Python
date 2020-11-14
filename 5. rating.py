my_list = [7, 5, 3, 3, 2]
for i in range(9):
    index_a = 0
    num = int(input('Please input number for rating'))
    if num in my_list:
        index_d = my_list.index(num) + my_list.count(num)
        my_list.insert(index_d, num)
    else:
        for index in range(len(my_list)):
            if num < my_list[index]:
                index_a = index + 1
        my_list.insert(index_a, num)
    print(my_list)
