file = 'zen.txt'
list1 = list()
with open(file) as f:
    for l in f:
        list1.append(l)
for i in range(len(list1) - 1, 0, -1):
    print(list1[i].rstrip())
