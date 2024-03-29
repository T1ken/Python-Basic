from random import randint, choice
NAMES = ['Гвидон', 'Женя', 'Иван-калыван', 'Виктор', 'Сеня', 'Федя']
SURNAMES = ['Чернявский', 'Зайцев', 'Сыендук', 'Шматко', 'Баринов']


def generate_person():
    name = choice(NAMES)
    surname = choice(SURNAMES)
    age = randint(20, 50)
    return name, surname, age


class Person:
    def __init__(self, name, surname, age):
        self.__name = name
        self.__surname = surname
        self.__age = age

    def __str__(self):
        return f'Меня зовут {self.__name} {self.__surname}. Мой возраст - {self.__age}'


class Employee(Person):
    def calc_salary(self):
        raise Exception('This method must be overriden')

    def __str__(self):
        return super().__str__() + f'\nМоя зарплата {self.calc_salary()}'


class Manager(Employee):
    def calc_salary(self):
        return 13000


class Agent(Employee):
    sales: int

    def calc_salary(self):
        return 5000 + .05 * self.sales


class Worker(Employee):
    hours: int

    def calc_salary(self):
        return 100 * self.hours


if __name__ == '__main__':
    employees = list()

    for _ in range(3):
        employees.append(Manager(*generate_person()))

    for _ in range(3):
        agent = Agent(*generate_person())
        agent.sales = randint(2000, 10000)
        employees.append(agent)

    for _ in range(3):
        worker = Worker(*generate_person())
        worker.hours = randint(20, 50)
        employees.append(worker)
    for emp in employees:
        print(emp)

# зачтено
