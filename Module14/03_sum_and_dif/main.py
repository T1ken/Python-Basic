def search_summ(num):
    summ_num = 0
    for i in str(num):
        summ_num += int(i)
    return summ_num


def search_num(num):
    summ_digit = 0
    for i in str(num):
        summ_digit += 1
    return summ_digit


ask = int(input())
print(search_summ(ask))
print(search_num(ask))
print(search_summ(ask) - search_num(ask))

# зачтено
