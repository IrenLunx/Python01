# Функция map() применяет указанную функцию к каждому элементу итерируемого объекта и возвращает итератор с новыми объектами

li = [x for x in range(1, 20)]
print(li)

li = list(map(lambda x: x + 10, li))
print(li)

data = list(map(int, input().split()))
print(data)

data = map(int, '1 2 3 66 77'.split())
for e in data: # по map можно пробежаться только 1 раз, поэтому лучше его сохранить, например, сразу в list
    print(e)

