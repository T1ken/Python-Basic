l = []
m = []
ask = int(input('Кол-во видеокарт: '))
for i in range(1, ask + 1):
    video_ask = int(input(f'{i} Видеокарта: '))
    l.append(video_ask)
for a in l:
    m.append(max(l))
m = max(l)
print(f'Старый список{l}')
print(f'Новый список {m}')

