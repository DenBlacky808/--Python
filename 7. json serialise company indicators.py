from functools import reduce
import json


def read_indicators(line_f):
    sym = [el for el in line_f if el.isdigit() or el == ' ']
    sym_2 = ''.join(sym).split()
    return int(sym_2[0]) - int(sym_2[1])


with open("text_7.txt", 'r', encoding='utf-8') as fi_1:
    my_indicators = {line[:line.find(" ")]: read_indicators(line) for line in fi_1.readlines()}
    list_to_json = [
        my_indicators,
        {
            'average_profit': reduce((lambda x, y: x + y if (x > 0 and y > 0) else x + 0), my_indicators.values()) / (
                    len(my_indicators) - ''.join(map(str, my_indicators.values())).count('-'))}
    ]
with open("text_707.json", 'w', encoding='utf-8') as fi_2:
    json.dump(list_to_json, fi_2, indent=4, sort_keys=True, ensure_ascii=False)
