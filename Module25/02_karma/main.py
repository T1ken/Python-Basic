from random import randint

karma = 0


def one_day():
    return randint(1, 7)


class KillError(Exception):
    pass


class DrunkError(Exception):
    pass


class CarCrashError(Exception):
    pass


class GluttonyError(Exception):
    pass


class DepressionError(Exception):
    pass


list1 = [KillError, DrunkError, CarCrashError, GluttonyError, DepressionError]
while True:

    v = randint(1, 10)
    k = randint(0, len(list1) - 1)
    karma += one_day()

    if v == 5:
        try:
            raise list1[k]

        except KillError:
            karma -= 100

        except DrunkError:
            karma -= 10

        except CarCrashError:
            karma = 0

        except GluttonyError:
            karma -= 5

        except DepressionError:
            karma -= 50
        print(list1[k].__name__)

    if karma == 500:
        break

print(karma)
