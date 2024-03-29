import os.path


def gen_files_path(folder, path=os.path.abspath(os.sep)):
    for elem in os.listdir(path):
        path_elem = os.path.join(os.path.abspath(path), elem)
        if os.path.isfile(path_elem):
            print(path_elem)
            continue
        elif folder == elem:
            print(f'\nКаталог {folder} найден.\nПуть к каталогу: {path_elem}')
        else:
            path_elem = gen_files_path(folder, path_elem)
            if path_elem:
                return path_elem


path_search = input(f'Введите путь поиска: ')
folder_search = input(f'Какой каталог ищем? ')
print(f'\nПути всех файлов\n')
if not gen_files_path(folder_search, path_search):
    print(f'\nКаталог {folder_search} не найден')

# Тебе для чего yield? У тебя модуль чему посвящён? Пофиг, зачтено
