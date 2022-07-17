# Множества
# Тип данных set

colors = {'red', 'green', 'blue'}
print(type(colors)) # <class 'set'>

colors.add('gray') # добавить элемент
print(colors)
colors.remove('red') # удалить элемент, если такого нет - будет ошибка
print(colors)
colors.discard('red') # удалить значения, но ошибки не будет, программа продолжит работу
print(colors)
colors.clear() # очистить множество и продолжить работу с пустым
print(colors)

a = {1, 2, 4, 6, 8}
b = {2, 4, 5, 7, 9}
c = a.copy() # Копия множества
u = a.union(b) # Объединение множеств
i = a.intersection(b) # Пересечение множеств
k = a.difference(b) # Разница первого множества со вторым
d = b.difference(a) # Разница второго множества с первым

q = a \
    .union(b) \
    .difference(a.intersection(b)) # Разница первого и второго множества

s = frozenset(a) # Замороженное множество, в него нельзя вносить изменения
