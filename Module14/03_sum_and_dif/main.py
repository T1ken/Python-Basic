def search_summ(num):
    summ_num = 0
    for i in str(num):
        summ_num += int(i)
    print(summ_num)


def search_num(num):
    summ_digit = 0
    for i in str(num):
        summ_digit += 1
    print(summ_digit)


ask = int(input())
search_summ(ask)
search_num(ask)

# Во-первых, опять принты и инпуты без информации. Во вторых, разность суммы и количества цифр не выводится.
