import random as r
list1 = list()
while True:
    s = r.randint(1, 14)
    ask = int(input('Введите число: '))
    list1.append(ask)
    if s == 13:
        print('Вас постигла неудача!')
        break
    with open('cipher.txt', 'w') as file:
        for line in list1:
            file.write(str(line) + '\n')
    if sum(list1) >= 777:
        print('Вы успешно выполнили условие для выхода из порочного цикла!')
        break
