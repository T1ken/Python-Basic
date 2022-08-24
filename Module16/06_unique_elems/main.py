lst_one = []
lst_two = []
ask_1 = int(input(f'Сколько чисел будет в первом списке? '))
for i in range(1, ask_1 + 1):
    number = int(input(f'Введите {str(i)}  число для первого списка: '))
    lst_one.append(number)
ask_2 = int(input(f'Сколько чисел будет во втором списке? '))
for i in range(1, ask_2 + 1):
    query = 'Введите ' + str(i + 1) + ' число для второго списка: '
    number = int(input(f'Введите {str(i)} число для второго списка: '))
    lst_two.append(number)
lst_one.extend(lst_two)
for _ in range(len(lst_one)):
    for i in lst_one:
        if lst_one.count(i) > 1:
            lst_one.remove(i)

print(f'Новый первый список с уникальными элементами: {lst_one}')

# Сказано же: условные операторы использовать нельзя (15 строчка шутка для тебя) (если что условные операторы это if elif else)
# пошел на хутор, как это говно делать
