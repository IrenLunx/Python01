# Доп.задача №2
# Проверить, является ли число простым

a = int(input('Введите натуральное число: '))
result = True
for i in range(a):
    if i > 1 and a % i == 0:
        result = False
if a < 1:
    print('Число не является натуральным!')
elif result == True:
    print(f'Число {a} является простым')
else:
    print(f'Число {a} не является простым')