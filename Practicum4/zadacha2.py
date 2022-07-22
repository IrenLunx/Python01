# Считать строку набора чисел из файла. Напишите программу, которая покажет большее и меньшее число.
# В качестве символа разделителя используйте пробел.

path = 'file.txt'
newList = ''
with open(path, 'r') as f:
    newList = f.readline()

newList = newList.split(' ')
print(newList)
min = int(newList[0])
max = int(newList[0])
for i in newList:
    if int(i) > max:
        max = int(i)
    elif int(i) < min:
        min = int(i)
print(min, max)