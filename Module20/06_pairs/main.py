origin_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
dict_pre = {}
for i in origin_list[0::2]:
    if len(dict_pre) == 0:
        dict_pre = {i: i + 1}
    else:
        dict_pre.update({i: i + 1})
tuple_list = [(key, value) for key, value in dict_pre.items()]
print(origin_list)
print(tuple_list)

# зачтено
