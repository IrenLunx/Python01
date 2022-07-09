# Доп.задача №3
# Найти наибольший простой делитель числа

a = int(input('Введите натуральное число: '))
number = 0
result = True
for j in range(a + 1):
    if j > 0 and a % j == 0:
        for i in range(j):
            if i > 1 and j % i == 0:
                result = False
                break
            else:
                result = True
        if result == True:
            number = j
if a < 1:
    print('Число не является натуральным!')
else:
    print(f'Число {number} является простым делителем')