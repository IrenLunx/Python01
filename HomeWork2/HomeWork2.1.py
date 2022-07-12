# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

def sumNumbers (number: int) -> int: 
    sumNum = 0
    if number < 0:
        number *= -1
    while number > 0:
        sumNum += number % 10
        number //= 10
    return(sumNum)

n = input('Введите вещественное число: ')
number = n.replace('.', '')
number = int(number)
print(f'Сумма чисел в числе {n} = {sumNumbers(number)}')