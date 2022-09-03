word = input('Введите строку: ').lower()
chars = list()
for i in word:
    if i in chars:
        chars.remove(i)
    else:
        chars.append(i)
if len(chars) > 1:
    print('Нельзя сделать полиндром')
else:
    print('Можно сделать полиндром')
# зачтено
