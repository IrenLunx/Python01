# Задана натуральная степень k. Сформировать случайным образом список коэффициентов 
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример: - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random

def fillListRandom(size: int):
    lisrStr = []
    for i in range(size):
        lisrStr.append(random.randrange(0, 100))
    return lisrStr

k = int(input('Введите число степени (от 1 и больше): '))
if k < 1:
    print('Введите число от 1!')
else:
    newList = fillListRandom(k + 1)
    print(newList)
    newStr = ''
    indexList = k + 1
    coeff = 1
    for i in range(k + 1):
        if i == 0:
            indexList -= 1
            newStr = str(newList[indexList]) + ' = 0' + newStr
        elif i == 1:
            indexList -= 1
            newStr = str(newList[indexList]) + '*x + ' + newStr
        else:
            indexList -= 1
            coeff += 1
            newStr = str(newList[indexList]) + '*x^' + str(coeff) + ' + ' + newStr
    print(newStr)

    path = 'HomeWork4/homeWork4.4.txt'
    with open(path, 'w') as f:
        f.write(newStr)