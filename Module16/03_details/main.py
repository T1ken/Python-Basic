shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300],
        ['педаль', 100], ['седло', 1500], ['рама', 12000],
        ['обод', 2000], ['шатун', 200], ['седло', 2700]]
det_cost = 0
det_count = 0
detail = input('Название детали: ')
det_counts = int(input('Кол-во деталей - '))
for i in range(len(shop)):
    if shop[i][0] == detail.lower():
        det_count += 1
        det_cost += shop[i][1]
if det_count > 0:
    print('Общая стоимость -', det_cost * det_counts)
else:
    print('Товар не найден.')
