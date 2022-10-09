nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]], [[11, 12, 13], [14, 15], [16, 17, 18]]]


def my_list(*args):
    lst = []
    for elem in args:
        for sub_elem in elem:
            if not isinstance(sub_elem, list):
                lst.append(sub_elem)
            else:
                result = my_list(sub_elem)
                lst.extend(result)
    return lst


print(my_list(nice_list))
