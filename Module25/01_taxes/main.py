sum_nalog = 0
amount_money = int(input('Введите количество имеющихся у вас денег: '))
price_1 = float(input('Ценник квартиры: '))
price_2 = float(input('Ценник Сar: '))
price_3 = float(input('Ценник дачи:: '))


class Property:

    def __init__(self, __worth=0):
        self.__worth = __worth

    def get_worth(self):
        return self.__worth

    def tax(self):
        return self.__worth   # какой мудак придумал именно два подчеркивания


class CountryHouse(Property):
    name = 'Дом'

    def __init__(self, worth):
        super().__init__(worth)

    def tax(self):
        return super().get_worth() / 500


class Apartment(Property):
    name = 'Квартира'

    def __init__(self, worth):
        super().__init__(worth)

    def tax(self):
        return super().get_worth() / 1000


class Car(Property):
    name = 'Сar'   # мы англичане, хули

    def __init__(self, worth):
        super().__init__(worth)

    def tax(self):
        return super().get_worth() / 200


tax_list = [Apartment(price_1), Car(price_2), CountryHouse(price_3)]
for elem in tax_list:
    print(f'Налог на {elem.name} составит {elem.tax()}')
    sum_nalog += elem.tax()
print(f'Сумма налога составила {sum_nalog}')
if sum_nalog > amount_money:
    print(f'Вам не хватает {sum_nalog - amount_money} для оплаты налогов') # чувствую себя мразью когда пишу такие коды, мне жаль людей, которые видят такое
# А вроде мне плевать, двоякое чувство
else:
    print(f"У вас получилось, осталось {amount_money - sum_nalog} наличных")
