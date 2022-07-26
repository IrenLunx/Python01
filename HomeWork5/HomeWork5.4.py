# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных
# Входные и выходные данные хранятся в отдельных текстовых файлах

path = 'HomeWork5/HomeWork5.4.1.txt'
with open(path, 'r') as f:
    data = f.read()
    print(data)

newStr = ''
countStr = 1
for i in range(1, len(data)):
    if data[i] == data[i - 1]:
        countStr += 1
        if i == len(data) - 1:
            newStr += str(countStr) + data[i]
    else:
        newStr += str(countStr) + data[i - 1]
        countStr = 1
print(newStr)

strValue = ''
newStr = list(newStr)
path2 = 'HomeWork5/HomeWork5.4.2.txt'
with open(path2, 'w') as f:
    for i in range(1, len(newStr), 2):
        strValue += int(newStr[i - 1]) * newStr[i]
    f.write(strValue)
