learn = input('Введите слово: ')
word = []
num = 0
for i in learn:
    if i not in word:
        num += 1
    elif i in word:
        num -= 1
    word.append(i)
if num < 0:
    num = 0
print(f'Кол-во уникальных букв: {num}')

# при введении слова "лава" выдаёт, что количество уникальных букв 3.
