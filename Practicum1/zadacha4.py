# Показать первую цифру дробной части числа

a = float(input('Введите дробное число: '))
a = a * 10 % 10
print(int(a))