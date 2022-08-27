import random
duration = int(input(f'Кол-во чисел в списке: '))
before = [random.randint(0, 2) for _ in range(duration)]
compress = [x for x in before if x > 0]
count = len(before) - len(compress)
print(f'Список до сжатия: {before}')
print('Список после сжатия:', compress)

# зачтено
