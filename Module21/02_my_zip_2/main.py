def myzip(*args):
    f_lst = [list(elem) for elem in args]
    length = min((len(elem) for elem in args))
    snd_lst = list(tuple(elem[i] for elem in f_lst)
                   for i in range(length))
    return snd_lst


_list = [1, 2, 'x', 'y', 'i']
_dict = {1: 'a', 2: 'b'}
_tuple = 1, 2, 'a', 'b'
_string = 'zxcobema'
_set = {1, 2, 'a', 'b'}
all_op = [_list, _dict, _tuple, _string, _set]
for p in all_op:
    print(myzip(p))
