import math


class Car:

    def __init__(self, x, y, fi):
        self.x = x
        self.y = y
        self.fi = fi

    def move(self, dist):
        self.x = self.x + dist * math.cos(self.fi)
        self.y = self.y + dist * math.sin(self.fi)


class Bus(Car):
    PAY_COEFF = 0.01
    max_pass = 60

    def __init__(self, x, y, direction):
        super().__init__(x, y, direction)
        self.passagers = 0
        self.money = 0

    def move(self, distance):
        self.money += Bus.PAY_COEFF * self.passagers * distance
        super().move(distance)

    def enter(self, passengers):
        if passengers + self.passagers >= Bus.max_pass:
            print('Достигнута максимальная вместимость автобуса')
            print(f'Уехать смогли только {Bus.max_pass - self.passagers}')
            print(f'Остались {passengers - (Bus.max_pass - self.passagers)}')
            passengers = Bus.max_pass - self.passagers
        return passengers

    def exit(self, passgers):
        if passgers > self.passagers:
            print('Вышли все из автобуса')
            passgers = self.passagers
        return passgers

    def __str__(self):

        lines = [
            super().__str__(),
            f'В автобусе {self.passagers} пассажиров',
            f'У водителя {round(self.money, 2)} денег',
        ]
        return '\n'.join(lines)
