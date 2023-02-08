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
            break

        except DrunkError:
            break

        except CarCrashError:
            break

        except GluttonyError:
            break

        except DepressionError:
            break

    if karma == 500:
        break

print(karma)

# ну так то ошибка в это игре = смерть (спасибо цензуре скилбокса. в моё время было написано прямо), соответственно,
# первая ошибка = выход из программы. так же посторайся оформить более интересную обработку ошибок для каждой отдельно.
