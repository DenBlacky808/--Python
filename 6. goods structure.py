number = 1
goods = []
name_list = []
price_list = []
quantity_list = []
unit_list = []
an_dict = {}
dict_load = {}
while True:
    print(' 1. - Add new goods.\n 2. - Show analytics.\n 3. - Exit. ')
    choice = int(input('Please choose what operation do you want? '))
    if choice == 1:
        goods_in = input('Input using space bar name price quantity and unit rev ')
        new_goods = goods_in.split()
        new_dict = {'name': new_goods[0], 'price': new_goods[1], 'quantity': new_goods[2], 'unit': new_goods[3]}
        new_tuple = (number, new_dict)
        number += 1
        goods.append(new_tuple)
    elif choice == 2:
        for dict_el in goods:
            dict_load = dict_el[1]
            for key, value in dict_load.items():
                if key == 'name':
                    name_list.append(value)
                elif key == 'price':
                    price_list.append(int(value))
                elif key == 'quantity':
                    quantity_list.append(int(value))
                elif key == 'unit':
                    unit_list.append(value)
        an_dict = {'name': name_list, 'price': price_list, 'quantity': quantity_list, 'unit': unit_list}
        print(an_dict)
        an_dict.clear()
        name_list.clear()
        price_list.clear()
        quantity_list.clear()
        unit_list.clear()
    elif choice == 3:
        break
    else:
        print('Please input number of your choice from 1 to 3')
