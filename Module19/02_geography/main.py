data_set = {}
amount_country = int(input('Кол-во стран: '))
for i in range(amount_country):
    value = input('{} страна: '.format(i + 1)).split()
    for city in value[1:]:
        data_set[city] = value[0]
for i in range(3):
    city = input(f'\n{i + 1} город: ')
    country = data_set.get(city)
    if city in data_set:
        print(f'Город {city.title()} расположен в стране {country.title()}.')
    else:
        print(f'По городу {city} данных нет.')
