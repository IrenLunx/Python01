# [exp for item in iterable]
# [exp for item in iterable (if conditional)]
# [exp <if conditional> for item in iterable (if conditional)]

newList = []

for i in range(1, 101):
    if i % 2 == 0:
        newList.append(i)

print(newList)

# Заполнение листа другой записью
newList2 = [i for i in range(1, 21)] # Все числа подряд
print(newList2)

newList3 = [i for i in range(1, 21) if i % 2 == 0] # Все четные числа
print(newList3)

newList4 = [(i, i) for i in range(1, 21) if i % 2 == 0] # Все четные кортежи
print(newList4)

def kub(x):
    return x**3

newList4 = [(i, kub(i)) for i in range(1, 21) if i % 2 == 0] # Все четные кортежи + функция возведения в куб
print(newList4)