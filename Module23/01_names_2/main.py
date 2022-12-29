with open('people.txt', encoding='UTF-8') as f:
    try:
        f = f.readlines()
        size = sum([len(i.strip()) for i in f])
        for x, i in enumerate(f, 1):
            if len(i.strip()) < 3:
                raise BaseException(f'Ошибка: менее трёх символов в строке {x}')
    except BaseException as q:
        print(q)
    finally:
        print('Общее количество символов:', size)
