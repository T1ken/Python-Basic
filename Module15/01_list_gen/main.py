i = 1
asd = []
num = int(input())
while i < num:
    if i + 2 >= num:
        break
    i += 2
    asd.append(i)
print(asd)

# Единица не попадает в список, и если ввести к примеру 11, оно тоже не попадёт.
