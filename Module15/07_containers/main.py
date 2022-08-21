def f(x):
    if x < 1 or x > 200:
        print('Вес: [1-200]')
        return False
    else:
        return True


n = int(input('Количество контейнеров: '))
while n <= 0:
    print('Введите число больше 0!')
    n = int(input('Количество контейнеров: '))
a = []
i = 0
while i < n:
    b = int(input('Введите вес контейнера: '))
    if f(b):
        a.append(b)
        i += 1
while True:
    X = int(input('Введите вес нового контейнера: '))
    if f(X): break
for i in range(n):
    if X >= a[i]:
        print(i + 1)
        break
