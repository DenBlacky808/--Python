def read_hours(line_f):
    sym = [el for el in line_f if el.isdigit() or el == ' ']
    sym_2 = ''.join(sym).split()
    return sum(map(int, sym_2))


with open("text_6.txt", 'r+', encoding='utf-8') as fi_1:
    print({line[:line.find(":")]: read_hours(line) for line in fi_1.readlines()})
