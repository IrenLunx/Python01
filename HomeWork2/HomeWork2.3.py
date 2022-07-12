# Задайте список из n чисел последовательности (1 + 1 / n) ^ n и выведите на экран их сумму.

def proizvedNumbers(n, proizved = 0):
    proizved += (1 + 1 / (n)) ** (n)
    return proizved

n = int(input('Введите число: '))
numList = ''
sumNum = 0
for i in range(1, n + 1):
    if i == n:
        numList += str(i) + ': ' + str(round(proizvedNumbers(i), 2))
    else:
        numList += str(i) + ': ' + str(round(proizvedNumbers(i), 2)) + ', '
    sumNum += round(proizvedNumbers(i), 2)

print(f'Для числа {n} сумма последовательности чисел: \n{numList} = {sumNum}')