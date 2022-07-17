# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример: - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def fibonacciNeg(n):
    if n == 1:
        return 1
    elif n == 0:
        return 0
    else:
        return fibonacciNeg(n + 2) - fibonacciNeg(n + 1)

n = int(input('Введите положительное число: '))
newList = []
for i in range(-n, n + 1):
    if i <= 0:
        newList += [fibonacciNeg(i)]
    elif i > 0:
        newList += [fibonacci(i)]
print(f'Список чисел Фибоначчи (с отрицательными индексами) для {n} = {newList}')