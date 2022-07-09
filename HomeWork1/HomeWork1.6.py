# Доп.задача №1
# Найти факториал числа

f = int(input('Введите число факториала: '))
result = 1
for i in range(f):
    result *= i + 1
print(f'Факториал числа {f} = {result}')