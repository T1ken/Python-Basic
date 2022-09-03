num_orders = int(input('Введите кол-во заказов: '))
orders_data = {}
for i in range(1, num_orders + 1):
    order = input(f'{i} заказ: ')
    fio, pizza, amount = order.rsplit()
    amount = int(amount)
    if fio not in orders_data:
        orders_data[fio] = {pizza: amount}
    else:
        if pizza not in orders_data[fio]:
            orders_data[fio][pizza] = amount
        else:
            orders_data[fio][pizza] += amount
for fio, order in sorted(orders_data.items()):
    print(f'{fio}:')
    for pizza, amount in sorted(order.items()):
        print('\t', pizza, amount)

# зачтено
