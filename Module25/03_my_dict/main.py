dict1 = {'qwe': 1, 'asd': 2, 'zxc': 993}
ask_dict = input('Введите то что вы ищете в словаре и бла бла бла')


class Get:
    def __init__(self, dct, ask):
        self.ask = ask
        self.dct = dct

    def g(self):
        if self.dct.get(self.ask) is None:
            return 0
        else:
            return self.dct.get(self.ask)


print(Get(dict1, ask_dict).g())

# совершенно непонятно, что и куда нужно вводить, инпут пустой, имена переменных и методов тоже не совсем понятные
# пошел нах
