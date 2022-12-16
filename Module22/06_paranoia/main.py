h = list()
y = list()
shift = 1
ascii_en = [chr(i) for i in range(ord('a'), ord('z') + 1)]
encrypted_string = list()
open('text.txt')
e = ''
text_ = 'text.txt'
with open(text_) as f:
    l = f.readlines()
    h.append(l)
for w in l:
    y.append(w.rstrip())


def get_index(smb, to_right, lst):
    index = lst.index(smb)
    if index + to_right > len(lst) - 1:
        index = index + to_right - len(lst)
    else:
        index += to_right
    return index


for symbol in y:
    symbol = symbol.lower()
    for i in symbol:
        if i in ascii_en:
            e += ascii_en[get_index(i, shift, ascii_en)]
        else:
            encrypted_string += symbol
    encrypted_string.append(e)
    shift += 1
    e = ''
with open('cipher_text.txt', 'w') as file:
    for line in encrypted_string:
        file.write(line + '\n')
