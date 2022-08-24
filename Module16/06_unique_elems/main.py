lst_one = [1, 2, 3]
lst_two = [2, 4, 6, 3, 3, 2, 1]
lst_one.extend(lst_two)
for _ in range(len(lst_one)):
    for i in lst_one:
        if lst_one.count(i) > 1:
            lst_one.remove(i)
print(lst_one)

# Сказано же: условные операторы использовать нельзя
