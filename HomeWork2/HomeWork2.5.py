# Реализуйте алгоритм перемешивания списка.

def listSort(n):
    for i in range(len(n) // 2):
        helpVar = n[i]
        n[i] = n[-i - 1]
        n[-i - 1] = helpVar

n = ['привет', 'дорогой', 'друг', 'я', 'рад', 'тебя', 'видеть']
listSort(n)
print(n)