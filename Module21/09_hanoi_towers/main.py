def move(n, x=1, y=3):

    def z(x=1, y=3):
        return ({1, 2, 3} - {x} - {y}).pop()
    if n:
        z = z(1, 3)
        move(n - 1, x, z)
        print(f'Переложить диск {n} со стержня номер {x} на стержень номер {y}')
        move(n - 1, z, y)


n = int(input('Введите количество дисков: '))
move(n)
