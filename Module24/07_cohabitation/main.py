from random import randint, choice


class House:
    food = 50
    money = 0


def repast():
    House.food += 1
    House.money -= 1
    return f'Идет в магазин, еда {House.food} деньги {House.money}'


class Person:

    def __init__(self, name):
        self.name = name
        self.satiety = 50

    def play(self):
        self.satiety -= 1
        return f'Играет, сытость {self.satiety}'

    def work(self):
        self.satiety -= 1
        House.money += 1
        return f'Работает, сытость {self.satiety} деньги {House.money}'

    def eat(self):
        self.satiety += 1
        House.food -= 1
        return f'Ест, сытость {self.satiety} еда {House.food}'


person_1 = Person('Сеня')
person_2 = Person('Федя')
for i in range(366):
    number_cubes = randint(1, 6)
    person = choice([person_1, person_2])
    if person.satiety < 0:
        print(f'К сожалению, {person.name} умер с голоду, по вине {person_2.name}, Иуды и предателя ')
        break
    if person.satiety < 20 and House.food >= 10:
        text = person.eat()
    elif House.food < 10:
        text = repast()
    elif number_cubes == 1:
        text = person.work()
    elif House.money < 50:
        text = person.work()
    elif number_cubes == 2:
        text = person.eat()
    else:
        text = person.play()
    print(person.name, text)

if i == 365:
    print('Сеня и Федя выжили, чудом')
else:
    print('Помянем огузков')
