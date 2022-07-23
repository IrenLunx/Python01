# В файле находится N натуральных чисел, записанных через пробел. 
# Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. Найти его.

path = 'HomeWork4/HomeWork4.7.txt'
with open(path, 'r') as f: data = f.read()

data = data.split(' ')
for i in range(1, len(data)):
    if int(data[i]) - 1 != int(data[i - 1]):
        print(f'Не хватает числа {i + 1}')
