import random as r
list1 = list()
try:
    while True:
        s = r.randint(1, 14)
        ask = int(input('Введите число: '))
        list1.append(ask)
        if s == 13:
            print('Вас постигла неудача!')
            raise ValueError()
        with open('cipher.txt', 'w') as file:
            for line in list1:
                file.write(str(line) + '\n')
                if sum(list1) >= 777:
                    print('Вы успешно выполнили условие для выхода из порочного цикла!')
                    raise ValueError
except ValueError:
    print(end='')
# У тебя раздел посвящён работе с ошибками, а ты выходишь из цикла брейком. Даже в тз написано - "исключение", т.е.
# надо использовать try/except.
