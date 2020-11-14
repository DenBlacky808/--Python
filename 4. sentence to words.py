sentence = input('Please input some sentence. ')
list_words = sentence.split()
for position, string in enumerate(list_words, 1):
    if len(string) > 10:
        print(position, string[:10])
    else:
        print(position, string)
