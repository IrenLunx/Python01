# Напишите программу, которая определит позицию второго вхождения строки в списке
# либо сообщит, что ее нет

list_str = ['ghj', '465jgjyy675', '556', 'ghj', '89', '56', 'ghj', 'ghj', 'ghj']
val_str = 'ghj'
countStr = -1
countIndex = 0
for i in list_str:
    if i == val_str:
        if countStr == 0:
            countStr = list_str[countIndex]
            break
        else:
            countStr += 1
    countIndex += 1
print(countIndex)

def countString(list_str, val_str): # решение с семинара
    index = -1
    for i in range(len(list_str)):
        if (list_str[i] == val_str):
            index = i
    print(index)