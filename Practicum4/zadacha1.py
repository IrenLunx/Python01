# файлы
# a = добавить и читать
# w = создает, если нет, но если есть - удалит и перезапишет
# r = только чтение

import os # или другая from pathlib import Path

path = 'file.txt' # path = 'Python' + os.sep + 'file.txt' 
# помогает в вопросе разделителя в пути (с библиотекой os) 
# или path = os.path.join('Python', 'file.txt')
with open(path, 'r') as f:
    data = f.readline() # data = f.read(5)
    print(data)

with open(path, 'w') as f:
    pass