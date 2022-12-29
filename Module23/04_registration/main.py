def answer(file_str):
    name, mail, age = file_str.split('')
    age = int(age)
    sym = ('@', '.')
    if name.isalpha() is False:
        raise NameError('NameError')
    if age not in range(10, 100):
        raise ValueError('ValueError')
    for char in sym:
        if char not in mail:
            raise SyntaxError('SyntaxError')
    return file


with open('registrations.txt', 'r', encoding='utf-8') as file, open('registration_bad.txt', 'a', encoding='utf-8') as error, open('registrations_good.txt', 'a', encoding='utf-8') as good:
    for str_in_file in file:
        try:
            str_file = answer(str_in_file)
        except (NameError, ValueError, SyntaxError) as e:
            error.write(str(e) + '\n')
        else:
            good.write(str_in_file + '\n')
