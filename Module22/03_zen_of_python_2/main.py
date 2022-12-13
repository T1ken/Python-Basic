file = 'zen.txt'
list1 = list()
num = 0
num2 = 0
with open(file) as f:
    for l in f:
        l = l.lower()
        l = l.split()
        list1.append(l)
for l_ in list1:
    num += len(l_)
    for ll in l_:
        for lll in ll:
            num2 += 1
print(f' str - {len(list1)}')
print(f' слова - {num}')
print(f' буквы - {num2}')
