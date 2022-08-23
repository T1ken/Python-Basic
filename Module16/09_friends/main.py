friends_list = []
friend = int(input(f'Кол-во друзей: '))
receipt = int(input(f'Долговых расписок: '))
for _ in range(friend):
    friends_list.append(0)
for number in range(receipt):
    print(f'{number + 1} расписка')
    to_who = int(input(f'Кому: '))
    from_who = int(input(f'От кого: '))
    how_much = int(input(f'Сколько: '))
    friends_list[from_who - 1] += how_much
    friends_list[to_who - 1] -= how_much

print(f'Баланс друзей:')
for index in range(len(friends_list)):
    print(f'{index + 1} : {friends_list[index]}')
