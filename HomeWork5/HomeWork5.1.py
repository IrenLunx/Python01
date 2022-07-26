# Напишите программу, удаляющую из текста все слова, содержащие "абв"

newTxt = 'забвение бывает временным когда абв это называется самозабвением'.split()
strTxt = 'абв'
count = 0
for i in newTxt:
    if strTxt in i:
        newTxt.pop(count)
    count += 1
print(newTxt) 