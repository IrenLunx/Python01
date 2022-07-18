# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

n = [2, 5, 7, 8, 9, 2, 5, 8, 9, 4, 7]
newList = []
for i in n:
    newValue = True
    for j in n:
        if i != j:
            if n[i] == n[j]:
                newValue = False
            if newValue == True:
                newList += [j]
print(newList)