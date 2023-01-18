import random


class Warrior:
    def __init__(self, name, health=100):
        self.name = name
        self.health = health

    def hit(self, target):
        if type(self) == type(target):
            target.health -= 20


warriors = [Warrior('Воин1'), Warrior('Воин2')]
while True:
    ask = input('Введите 1, чтобы какой-то воин атаковал. Для закрытия программы введите 2: ')
    i = random.randint(0, 1)
    if ask == '1':
        attacker, victim = warriors[i], warriors[i - 1]
        attacker.hit(victim)
        print(f'{attacker.name} атаковал {victim.name}')
        print(f'У {victim.name} осталось здоровья {victim.health}')
        if victim.health == 0:
            print(f'{attacker.name} победил!')
            break
    elif ask == '2':
        break
    else:
        print(f'Ошибка ввода')
