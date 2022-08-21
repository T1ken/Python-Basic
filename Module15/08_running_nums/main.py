task = []
number = int(input('Сколько будет элементов в списке: '))
for i in range(number):
    task_id = int(input('Введите элемент списка: '))
    task.append(task_id)
print('Изначальный список:', task)
shift = int(input('Сдвиг: '))
task = task[-shift:] + task[:-shift]
print('Сдвинутый список:', task)
