def caesar(letter, shift):
    alphabet = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvw xyz'
    if letter.isupper():
        letter = letter.lower()
        position = alphabet.find(letter)
        return alphabet[position + shift].upper()
    else:
        letter = letter.lower()
        position = alphabet.find(letter)
        return alphabet[position + shift]


text_file = open('text.txt', 'r')
caesar_file = open('cipher_text.txt', 'w')

shift_size = 1
for line in text_file:
    string = ''
    for symbol in line:
        if symbol == '\n':
            break
        string = string + caesar(symbol, shift_size)
        caesar_file.write(string + '\n')
        shift_size += 1
