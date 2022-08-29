import string


def reverse_word(words):
    return ''.join(reversed(words))


text = input('Сообщение: ').split()
result = []
for word in text:
    word_part = ''
    word_back = ''
    for sym in word:
        if sym not in string.punctuation:
            word_part += sym
        else:
            word_back += reverse_word(word_part) + sym
            word_part = ''
    word_back += reverse_word(word_part)
    result.append(word_back)
print('Новое сообщение:', *result, sep=' ')

# зачтено
