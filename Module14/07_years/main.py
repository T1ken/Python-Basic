year_1 = int(input())
year_2 = int(input())
for i in range(year_1, year_2 + 1):
    for j in range(10):
        if str(i).count(str(j)) == 3:
            print(i)

# зачтено
