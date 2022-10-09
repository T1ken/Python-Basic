def fibonacci(n):
    if n in (1, 2):
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)
 

ask_num = int(input('Введите позицию числа в ряде Фибоначчи: '))
print(fibonacci(ask_num))
