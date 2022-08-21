films = ['Крепкий орешек', 'Назад в будущее', 'Таксист',
         'Леон', 'Богемская рапсодия', 'Город грехов',
         'Мементо', 'Отступники', 'Деревня']
favourites_films = []
films_number = int(input('Сколько фильмов хотите добавить? '))
for i in range(1, films_number + 1):
    movie = input('Введите название фильма: ')
    if movie not in films:
        print(f'Ошибка: фильма {movie} у нас нет :(')
    else:
        favourites_films.append(movie)
favourites_films = ''.join(favourites_films)
print('Список любимых фильмов:', favourites_films)
