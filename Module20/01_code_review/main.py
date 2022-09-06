students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology, swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}


def f(dick):
    lst = []
    string = ''
    for I in dick:
        lst += (dick[I]['interests'])
        string += dick[I]['surname']
    cnt = 0
    for _ in string:
        cnt += 1
    return lst, cnt


pairs = dict()
for i in students:
    pairs[i] = (students[i]['age'])
my_lst = f(students)[0]
l = f(students)[1]
print(f'Список пар "ID студента — возраст": {pairs}')
print(f'Полный список интересов всех студентов: {my_lst}')
print(f'Общая длина всех фамилий студентов: {l}')

# зачтено
