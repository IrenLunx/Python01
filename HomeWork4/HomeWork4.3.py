# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

n = [2, 5, 7, 8, 9, 2, 5, 8, 9, 4, 7]
n = set(n)
n = list(n) # конвертирую т.к. по условию нужен список
print(n)

# Если нужен список тех элементов, которые не повторялись ни разу в списке, то решение другое
d = [1, 2, 2, 2, 2, 3, 4, 4, 7, 0, 10]
newList = []
for i in range(len(d)):
    trueFalse = True
    for j in range(len(d)):
        if i != j:
            if d[i] == d[j]:
                trueFalse = False
                break
    if trueFalse: newList += [d[i]]
print(newList) 