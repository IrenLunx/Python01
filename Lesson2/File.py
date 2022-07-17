# Файлы. Связать файловую переменную с файлом, определив модификатор работы
# a - открытие для добавления данных (добавит к старым данным)
# r - открытие для чтения файлов
# w - открытие для записи данных (перезапишет прошлые данные, если были)
# w+, r+

colors = ['red', 'green', 'blue']
data = open('file.txt', 'a')
data.writelines(colors) # разделителей не будет (запись)
data.write('\nLINE 1\n') # добавление и новая строка
data.close()

# другой способ работы с файлом
with open('file.txt', 'w') as data:
  data.write('line 1\n')
  data.write('line 2\n')

# exit() # позволяет не выполнять код, который написан дальше
path = 'file.txt'
data = open(path, 'r')
for line in data:
    print(line)
data.close()