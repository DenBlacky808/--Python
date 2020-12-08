result_list = []


def int_func(some_word):
    new_char = ord(some_word[0]) - 32
    some_word_2 = chr(new_char) + some_word[1:]
    return some_word_2


input_string = input('Введите список слов через пробел ')
words_list = input_string.split()
words_list_2 = words_list[:]
for word in words_list:
    for letter in word:
        if 97 <= ord(letter) <= 122:
            pass
        else:
            try:
                words_list_2.remove(word)
            except ValueError:
                pass
for word_2 in words_list_2:
    result_list.append(int_func(word_2))

print(result_list)
