# Найти максимальное из пяти чисел

mas = [1, 2, 5, 3, 9, 5, 1]
max = mas[0]
for i in mas:
    if i > max:
        max = i
print(max)