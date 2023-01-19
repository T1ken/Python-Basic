import random


class Child:
    calm_states = {0: 'спокоен ', 1: 'плачет '}
    hungry_states = {0: 'сыт ', 1: 'голоден '}

    def __init__(self, child_name, child_age):
        self.name = child_name
        self.age = child_age
        self.calm_state = 0
        self.hungry_state = 0

    def child_info(self):
        print(f'Ребенку {self.name} {self.age} год, ')
        print(f'Ребенок {self.name} сейчас {Child.calm_states[self.calm_state]}')
        print(f'Ребенок {self.name} сейчас {Child.hungry_states[self.hungry_state]}')


class Parent:

    def __init__(self, parent_name, parent_age, children, children_count):
        self.children_count = children_count
        self.children = children
        self.name = parent_name
        self.age = parent_age
        self.children = []
        self.children_count = 0

    def parent_info(self):
        print(f'Меня зовут {self.name}, мне {self.age} год, у меня {self.children_count} детей:')
        for i_child in self.children:
            i_child.child_info()
        print()

    def soothe_the_child(self, child):
        if child.calm_state == 1:
            print(f' {self.name} успокаивает {child.name} ')
            child.calm_state = 0
        else:
            print(f' {child.name} спокоен ')

    def feed_the_child(self, child):
        if child.hungry_state == 1:
            print(f' {self.name} кормит {child.name} ')
            child.hungry_state = 0
        else:
            print(f'{child.name} сыт ')


parentName = input('Как зовут родителя? ')
parentAge = int(input(f'Сколько {parentName} лет? '))
parent = Parent(parentName, parentAge, children=[], children_count=0)

child_Name = input('Как зовут ребенка? ')
child_Age = int(input(f'Сколько {child_Name} лет? '))
child_1 = Child(child_Name, child_Age)
parent.children.append(child_1)
parent.children_count += 1
parent.parent_info()

for i_child in parent.children:
    i_child.calm_state = random.randint(0, 1)
    i_child.hungry_state = random.randint(0, 1)
    i_child.child_info()
    parent.soothe_the_child(i_child)
    parent.feed_the_child(i_child)

# Нет проверки на разницу в возрасте между родителем и ребёнком
