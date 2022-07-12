# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. Позиции задает пользователь через пробел (корректировка от преподавателя!)

n = int(input('Введите число n: '))
n = range(-n, n + 1)
n = list(n)
nIndex = input('Введите индексы элементов через пробел: ')
nIndex = nIndex.replace(' ', '')
nIndex = list(nIndex)

proizvedNum = 1
for i in nIndex:
    proizvedNum *= n[int(i)]
print(f'Произведение элементов на позициях {nIndex} = {proizvedNum}')