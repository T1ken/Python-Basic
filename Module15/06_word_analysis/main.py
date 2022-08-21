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

# при введении слова "облоко" выводит результат 2, хотя он равен 3. Сделай по моему способу с 2 списками.
