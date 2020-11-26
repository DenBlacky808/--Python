from googletrans import Translator

while True:
    try:
        with open("text_4.txt", 'r', encoding='utf-8') as fi_1:
            input('Нажмите Enter для перевода ')
            clean_list = sum([word.split() for word in [line.rstrip() for line in fi_1.readlines()]], [])
            en_words = [clean_list[i] for i in range(0, len(clean_list), 3)]
            words = [rus_w.text for rus_w in Translator().translate(en_words, dest='ru')]
            new_list = [f'{words[int(b / 3)]} {clean_list[b + 1]} {clean_list[b + 2]}\n' for b in
                        range(0, len(clean_list), 3)]
            break
    except AttributeError:
        print('С google translate нужны еще попытки) ')
with open("text_4_translated.txt", 'w', encoding='utf-8') as fi_2:
    fi_2.writelines(new_list)
