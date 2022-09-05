def cortej(incoming_list, number):
    if number not in incoming_list:
        return ()
    if incoming_list.count(number) == 1:

        return incoming_list[incoming_list.index(number):]
    return incoming_list[incoming_list.index(number):incoming_list.index(number, incoming_list.index(number) + 1) + 1]


print(cortej((1, 2, 3, 4, 5, 6, 7, 8, 2, 2, 9, 10), 1))
