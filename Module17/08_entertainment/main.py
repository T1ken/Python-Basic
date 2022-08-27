stick = list('I' * int(input(f'Кол-во палок: ')))
stick_run = int(input(f'Кол-во бросков: '))
for i in range(1, stick_run + 1):
    ask = int(input(f'Бросок {i}. Сбиты палки с номера '))
    ask2 = int(input(f'по номер '))
    for zxc in range(ask - 1, ask2):
        stick[zxc] = '.'
print(f'Результат: {"".join(stick)}')

# зачтено
