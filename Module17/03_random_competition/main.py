import random


def gen_list(size, start, end):
    lst = [round(random.uniform(start, end), 2) for x in range(size)]
    return lst


dimension = 20
fst_team = gen_list(dimension, 5, 10)
sec_team = gen_list(dimension, 5, 10)
battle = [(fst_team[i] if fst_team[i] > sec_team[i] else sec_team[i]) for i in range(dimension)]
print('Первая команда:', fst_team)
print('Вторая команда:', sec_team)
print('Победители тура:', battle)
