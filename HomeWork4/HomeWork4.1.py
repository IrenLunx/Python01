# Вычислить число pi c заданной точностью d 
# Пример: - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

def numberPi() -> float: 
    result = 3
    num = 4
    num2 = 2
    while num2 != 3002:
        result += (num / (num2 * (num2 + 1) * (num2 + 2))) - (num / ((num2 + 2) * (num2 + 3) * (num2 + 4)))
        num2 += 4
    return result

def decimalPlaces(number: str) -> int:
    number = abs(number.find('.') - len(number)) - 1
    return number

d = input('Введите точность числа pi от 0.1 до 0.0000000001: ')
if float(d) <= 0.1 and float(d) >= 0.0000000001:
    newStr = str(numberPi())
    d = decimalPlaces(d)
    newStr = float(newStr[:d + 2])
    print(newStr)
else:
    print('Вы вышли из заданного диапазона!')