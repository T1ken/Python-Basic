vowels = []
all_vowels = ['а', 'у', 'о', 'ы', 'и', 'э', 'е', 'я']
text = input('Введите текст: ')
for i in text:
    if i in all_vowels:
        vowels.append(i)
print(vowels)

# Не выводится длина, но ок, зачтено
