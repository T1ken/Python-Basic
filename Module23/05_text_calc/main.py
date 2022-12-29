result = []
with open('calc.txt', 'r') as file:
    for line in file.readlines():
        try:
            result.append(eval(line))
        except:
            ask = input(f'Обнаружена ошибка в {line}   Хотите исправить? ')
            if ask == 'да':
                line = input('Введите исправленную строку: ')
                result.append(eval(line))
print(f'Сумма результатов: {sum(result)}')
