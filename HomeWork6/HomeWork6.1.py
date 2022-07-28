# Доделать реализацию функции eval со скобками

def pluStr(newStr: str) -> float:
    result = 0
    newStr = newStr.split('+')
    result += float(newStr[0]) + float(newStr[1])
    return result

def minuStr(newStr: str) -> float:
    result = 0
    newStr = newStr.split('-')
    result += float(newStr[0]) - float(newStr[1])
    return result

def multiStr(newStr: str):
    result = 0
    newStr = newStr.split('*')
    if newStr[0][0] == '-' and newStr[1][0] == '-':
        return '+' + str(float(newStr[0]) * float(newStr[1]))
    else:    
        result += float(newStr[0]) * float(newStr[1])
        return result

def diviStr(newStr: str) -> float:
    result = 0
    newStr = newStr.split('/')
    result += float(newStr[0]) / float(newStr[1])
    return result

def resultStr(newStr: str) -> float:
    if newStr.index('-') == 0: return float(newStr)
    elif '-' in newStr: return minuStr(newStr)

newStr = '2*3/4+(6-2)/2-23*(-1)'
for i in range(len(newStr)):
    if '(' and ')' in newStr:
        one = newStr.index('(')
        two = newStr.index(')') + 1
        newStr = newStr.replace(f'{newStr[one:two]}', f'{resultStr(newStr[one + 1:two - 1])}')
    else:
        three = newStr.index('/')
        newStr = newStr.replace(f'{newStr[:three]}', f'{multiStr(newStr[:three])}')

        three = newStr.index('+')
        newStr = newStr.replace(f'{newStr[:three]}', f'{diviStr(newStr[:three])}')

        three = newStr.index('+') + 1
        four = newStr.index('-')
        newStr = newStr.replace(f'{newStr[three:four]}', f'{diviStr(newStr[three:four])}')

        three = newStr.index('-')
        newStr = newStr.replace(f'{newStr[three:]}', f'{multiStr(newStr[three:])}')

        three = newStr.index('+') + 1
        newStr = newStr.replace(f'{newStr[three:]}', f'{pluStr(newStr[three:])}')

        newStr = pluStr(newStr)
        break
print(newStr)