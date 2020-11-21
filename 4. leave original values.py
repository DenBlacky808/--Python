my_list_1 = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
my_list_2 = [my_list_1[i] for i in range(len(my_list_1)) if my_list_1.count(my_list_1[i]) == 1]
print(my_list_2)
