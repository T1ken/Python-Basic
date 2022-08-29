break_symbol = '@', '№', '$', '%', '^', '&', '*', '(', ')'
while True:
    ask = input(f'Название файла: ')
    if ask.startswith(break_symbol):
        print(f'Ошибка: название начинается на один из специальных символов.')
    if not ask.endswith('.txt') and not ask.endswith('.docx'):
        print(f'Ошибка: неверное расширение файла. Ожидалось .txt или .docx.')
    else:
        print(f'Файл назван верно.')
        break

# Зачтено. Только одно непонятно - зачем знаки форматирования перед строками
