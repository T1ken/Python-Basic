import zipfile
num = 0
ascii_en = [chr(i) for i in range(ord('a'), ord('z') + 1)]
ascii_ru = [chr(i) for i in range(ord('а'), ord('я') + 1)]
AScil_en = [chr(i) for i in range(ord('А'), ord('Я') + 1)]
AScil_ru = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
ascii_ = ascii_ru + ascii_en + AScil_ru + AScil_en
dictionary = {}
with zipfile.ZipFile("voyna-i-mir.zip") as archive:
    for filename in archive.filelist:
        with archive.open(filename) as file:
            for letter in file.read().decode():
                if letter not in dictionary:
                    letter = letter
                    dictionary[letter] = 0
                dictionary[letter] += 1
                num += 1
list1 = dict()
for letter, amount in dictionary.items():
    if letter in ascii_:
        list1[letter] = amount
q = {k: v for k, v in sorted(list1.items(), key=lambda item: item[1])}
for k, l in q.items():
    print(k, l)

# зачтено
# еще раз ты такое с тз сделаешь, я найду тебя и сломаю колени
