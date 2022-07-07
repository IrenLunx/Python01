# while

original = 23
inverted = 0
while original != 0:
    inverted = inverted * 10 + (original % 10)
    original //= 10
print(inverted)

# while else

original = 23
inverted = 0
while original != 0:
    inverted = inverted * 10 + (original % 10)
    original //= 10
else:
    print('Пожалуй,')
    print('хватит')
print(inverted)

# for i in enumeration:

for i in 1, 2, 3, 4, 5:
    print(i ** 2)

r = range(10) # r = range(1, 10) диапазон, r = range(1, 10, 2) через один 
for i in r:
    print(i)

for i in 'qev - jgj':
    print(i)

