list_orig = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_list = [list_orig[i + 1] for i in range(len(list_orig) - 1) if list_orig[i + 1] > list_orig[i]]
print(new_list)
