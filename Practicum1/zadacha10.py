# Найти расстояние между двумя точками пространства

x1 = int(input('Введите координату х первой точки: '))
y1 = int(input('Введите координату y первой точки: '))
x2 = int(input('Введите координату х второй точки: '))
y2 = int(input('Введите координату y второй точки: '))
sqrt = round(((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1)) ** 0.5, 3)
print(f'Расстояние между точками: ({x1}, {y1}) и ({x2}, {y2}) = {sqrt}')
