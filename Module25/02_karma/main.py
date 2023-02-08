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

# в итоге, вместо расширения обработок и логов, ты удалил их полностью. Добавь принты для каждой ошибки, в которой будет
# поясняться. что произошло. А зная тебя, ты можешь и ещё что-то интересней придумать
