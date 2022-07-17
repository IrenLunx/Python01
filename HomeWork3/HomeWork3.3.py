# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и 
# минимальным значением дробной части элементов.
# Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19

n = [1.55, 5.88, 9.99, 55.6, -3.455, -4.0, 60.0]
min = abs(float(n[0]) - int(n[0]))
max = abs(float(n[0]) - int(n[0]))
interValue = 0

for i in n:
    interValue = abs(float(i) - int(i))
    if interValue != 0:
        if interValue < min:
            min = interValue
        elif interValue > max:
            max = interValue

diffMaxMin = max - min
print(f'Разница между максимальным и минимальным значениями дробной части элементов: {round(diffMaxMin, 6)}')