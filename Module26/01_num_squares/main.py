class MyIter:
    def __init__(self, n):
        self.count = 0
        self.num = n

    def __iter__(self):
        return self

    def __next__(self):
        self.count += 1
        if self.count == self.num + 1:
            raise StopIteration
        else:
            return f'{self.count} ** 2 = {self.count ** 2}'


iter_object = MyIter(10)
for i in iter_object:
    print(i)

# ТЗ звучит так: "Реализацию напишите тремя способами: класс-итератор, функция-генератор и генераторное выражение".
# В твоей реализации есть только класс-итератор. Добавь функцию-генератор (с помощью yield) и генераторное выражение
# (как list comprehension, только в круглых скобках).
