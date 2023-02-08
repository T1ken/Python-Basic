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
            print('Ай ай ай ай убили негра, убили негра')
            break

        except DrunkError:
            print('Сдох потому что много пил')
            break

        except CarCrashError:
            print('Въебался в дерево потому что смотрел аниме за рулем, аниме убивает')
            break

        except GluttonyError:
            print('Помер и помер, че бубнить')
            break

        except DepressionError:
            print('Умер от депрессии')
            break

    if karma == 500:
        break

print(karma)

# зачтено
