class Storage:
    MAX_POS_FOR_EACH = 50


class OffEquip:
    name = 'some name'
    quantity = 0
    total_price = 0
    broken_in_service = 0
    in_dep = {}

    def ship_eq(self):
        print('1 - Sales; 2 - Administration; 3 - Project dep.; 4 - Storage')
        dep_from = input('Enter the department number, where do we ship the equipment from? ')
        dep_to = input('Please enter the department number, where do we ship the equipment to? ')
        data = input('How many pieces of equipment are we transferring to?')
        try:
            if int(self.in_dep[dep_from]) < int(data):
                print(f'Not enough {self.name} in dep! Check info before! ')
            else:
                if dep_from.isdigit() and dep_to.isdigit() and data.isdigit():
                    self.in_dep[str(dep_from)] = int(self.in_dep[dep_from]) - int(data)
                    self.in_dep[str(dep_to)] = int(self.in_dep[dep_to]) + int(data)
                    if self.in_dep['4'] > Storage.MAX_POS_FOR_EACH:
                        print('Too much items in storage. ')
                else:
                    print('Please input correct numbers ')
        except ValueError:
            print('Please input correct numbers ')

    def show_info(self):
        print(f'{self.name}\nIn sales department: {self.in_dep["1"]}\n'
              f'In administration department: {self.in_dep["2"]}\n'
              f'In project dep. department: {self.in_dep["3"]}\n'
              f'In storage : {self.in_dep["4"]}\n')


class Printers(OffEquip):
    def __init__(self):
        self.name = 'Printers'
        self.quantity = 100
        self.broken_in_service = 20
        self.total_price = 200000
        self.in_dep = {'1': 20, '2': 30, '3': 10, '4': 20}


class Scanners(OffEquip):
    def __init__(self):
        self.name = 'Scanners'
        self.quantity = 50
        self.broken_in_service = 10
        self.total_price = 200000
        self.in_dep = {'1': 10, '2': 15, '3': 5, '4': 10}


class Xerox(OffEquip):
    def __init__(self):
        self.name = 'Xerox'
        self.quantity = 25
        self.broken_in_service = 5
        self.total_price = 1000000
        self.in_dep = {'1': 5, '2': 5, '3': 3, '4': 7}


pr_1 = Printers()
sc_1 = Scanners()
xx_1 = Xerox()
menu_1 = 0
key = True
while key is True:
    menu_1 = input('MENU\nPrinters Transfer - 1\nScanners Transfer - 2\nXerox Transfer - 3\n'
                   '**********************\n'
                   'Printers show info - 4\nScanners show info - 5\nXerox show info - 6\nQuit - 7\n  '
                   'Please input number of type command: ')
    if menu_1 == '1':
        pr_1.ship_eq()
    elif menu_1 == '2':
        sc_1.ship_eq()
    elif menu_1 == '3':
        xx_1.ship_eq()
    elif menu_1 == '4':
        pr_1.show_info()
    elif menu_1 == '5':
        sc_1.show_info()
    elif menu_1 == '6':
        xx_1.show_info()
    elif menu_1 == '7':
        key = False
