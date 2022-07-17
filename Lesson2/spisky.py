
list1 = [1, 5, 8, 24, 67]
list2 = list1

list1[0] = 123
list2[1] = 15

for e in list1:
    print(e)

print()

for e in list2:
    print(e)

print(list1.pop()) # Извлекает (удаляет) последний элемент
print(list1)
print(list1.pop(2))
print(list1)
list1.insert(2, 11) # Добавляет элемент в список (сначала позиция, потом элемент)
print(list1)
list1.append(78) # Добавление в конец
print(list1)
