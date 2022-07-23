# Создать текстовый файл (не программно). Построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк). 
# Определить, кто из сотрудников имеет оклад менее 20 тысяч, вывести фамилии этих сотрудников. 
# Выполнить подсчёт средней величины дохода сотрудников.
# Пример файла:
# Иванов 23543.12
# Петров 13749.32

path = 'HomeWork4.6.txt'
with open(path, 'r', encoding = 'utf-8') as f:
    data = f.read()
    data = data.split('\n')

sumNum = 0
countNum = 0
for i in range(len(data)):
    countSum = data[i].split(' ')
    if float(countSum[1]) < 20000.0:
        print(countSum[0])
    sumNum += float(countSum[1])
    countNum += 1
result = sumNum / countNum
print(f'Средняя величина дохода сотрудников = {round(result, 2)}')
