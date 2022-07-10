# Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.
# Пример: - Для N = 5: 1, -3, 9, -27, 81

def searchNumber(a, b):
    for i in range(a):
        print(b)
        b *= -3

n = int(input('Введите число: '))
result = 1
searchNumber(n, result)
