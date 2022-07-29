# Напишите программу, удаляющую из текста все слова, содержащие "абв"

newTxt = 'забвение бывает временным когда абв это называется самозабвением'.split()
my_str = 'абв'
result = list(filter(lambda x: not my_str in x, newTxt))
print(result)