guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']
sleep = True
while sleep:
    print(f'Сейчас на вечеринке {len(guests)} человек: {guests}')
    ask = input(f'Гость пришел или ушел? ')
    if ask == 'пора спать':
        print(f'Вечеринка закончилась, все легли спать.')
        sleep = False
    else:
        name = input(f'Имя гостя: ')
        if ask == 'пришел':
            guests.append(name)
            if len(guests) > 6:
                print(f'Мест нет, идите нахуй')
                guests.remove(name)
            else:
                print(f'Привет {name}')
        if ask == 'ушел':
            print(f'Пока {name}')
            guests.remove(name)
