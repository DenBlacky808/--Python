class ExceptNonDigit(Exception):
    def __init__(self, txt):
        self.txt = txt


symbol = ''
digits_list = []
while symbol != 'stop':
    try:
        symbol = input('Введите числа для ввода в список, для выхода введите stop: ')
        if symbol.isdigit():
            digits_list.append(symbol)
        else:
            raise ExceptNonDigit('В список добавляются только числа!')
    except ExceptNonDigit as err:
        print(err)
print(digits_list)
