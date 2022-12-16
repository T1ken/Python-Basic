s = str()
file = 'numbers.txt'
with open(file) as f:
    for l in f:
        s += l
num = 0
s = s.split()
for i in s:
    num += int(i)
file_ = 'answer.txt'
with open(file_, 'w') as f_:
    f_.write(str(num))

# зачтено
