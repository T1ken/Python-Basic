number = int(input('Кол-во чисел: '))
app = []
for i in range(number):
    app.append(int(input('Число: ')))
counter = 0
while app != app[::-1]:
    app.insert(number, app[counter])
    counter += 1
print('Нужно приписать чисел:', counter)
print('Сами числа:', app[:counter][::-1])
# А где?
# исчезло, куда хз, я его делал
# зачтено
