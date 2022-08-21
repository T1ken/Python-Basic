learn = input('Введите слово: ')
word = []
num = 0
for i in learn:
    if i not in word:
        num += 1
    word.append(i)
print(f'Кол-во уникальных букв: {num}')
