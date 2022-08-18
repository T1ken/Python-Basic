x = float(input())
y = float(input())
r = int(input())
if (x ** 2 + y ** 2) ** 0.5 <= r:
    print('Рядом')
else:
    print('Не рядом')
