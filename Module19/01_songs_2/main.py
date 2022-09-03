violator_songs = {
    'World in My Eyes': 4.86,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.9,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.20,
    'Policy of Truth': 4.76,
    'Blue Dress': 4.29,
    'Clean': 5.83
}
all_num = 0
ask_num = int(input(f'Сколько песен выбрать? '))
for i in range(1, ask_num + 1):
    ask_song = input(f'Название {i} песни: ')
    if ask_song in violator_songs:
        all_num += violator_songs.get(ask_song)
    else:
        print(f'Песни нет в списке')
print(f'Общее время звучания песен: {round(all_num, 2)} минут')

# зачтено
