def tpl_sort(cort):
    mylist = cort
    if all(type(item) == int
           for item in mylist):
        return sorted(mylist)
    else:
        return mylist


zxc = (6, 3, -1, 8, 4, 10, -5)
print(*tpl_sort(zxc))

# зачтено
