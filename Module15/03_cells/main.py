cell = int(input(f'Кол-во клеток:'))
zxc = []
asd = []
a = 1
for i in range(1, cell + 1):
    ask = int(input(f'Эффективность {i} клетки: '))
    asd.append(ask)
for q in asd:
    if q < a:
        zxc.append(q)
    a += 1
zxc = str(zxc)
not_num = ''.join(zxc)
print('Неподходящие числа ', not_num)
