a = input()
b = input().split()
g = ((a[i], b[i]) for i in range(min(len(a), len(b))))
print(g)
print(*g, sep='\n')

# зачтено
