ask_num = int(input(f'Кол-во коньков: '))
asd = []
qwe = []
num = 0
for i in range(1, ask_num + 1):
    ask = input(f'Размер {i} пары: ')
    asd.append(ask)
ask_man = int(input(f'Кол-во людей: '))
for a in range(1, ask_man + 1):
    ask_man_num = input(f'Размер ноги {a} человека: ')
    qwe.append(ask_man_num)
for qw in qwe:
    if qw in asd:
        asd.remove(qw)
        num += 1
print(f'Наибольшее кол-во людей, которые могут взять ролики: {num}')

# зачтено
