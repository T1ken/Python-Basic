import zipfile
num = 0
ascii_en = [chr(i) for i in range(ord('a'), ord('z') + 1)]
ascii_ru = [chr(i) for i in range(ord('а'), ord('я') + 1)]
ascii_ = ascii_ru + ascii_en
dictionary = {}
with zipfile.ZipFile("voyna-i-mir.zip") as archive:
    for filename in archive.filelist:
        with archive.open(filename) as file:
            for letter in file.read().decode():
                if letter not in dictionary:
                    letter = letter.lower()
                    dictionary[letter] = 0
                dictionary[letter] += 1
                num += 1
for letter, amount in dictionary.items():
    letter.lower()
    if letter in ascii_:
        print(letter, amount)
# толстой, ты ебанутый
# я кст тоже, у меня в книге больше 100%
