word = input('Введите слово: ')
unique = 0
for letter in word:
    count = 0
    for i in word:
        if letter == i:
            count += 1
    if count == 1:
        unique += 1
print('Кол-во уникальных букв:', unique)

# зачтено
