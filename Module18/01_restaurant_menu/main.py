menu = 'утиное филе;фланк-стейк;банановый пирог;плов'
print(menu)
all_menu = ''
menu = menu.split(';')
all_menu += ', '.join(menu)
print(f'На данный момент в меню есть: {all_menu}')

# Зачтено
