# list = list списки введение

numbers = [1, 2, 3, 4, 5]
print(numbers) # [1, 2, 3, 4, 5]
ran = range(1, 6)
print(type(ran))
numbers = list(ran)
print(type(numbers))

print(numbers) # [1, 2, 3, 4, 5]

numbers[0] = 10

print(f'{len(numbers)} len') # длина с использованием интерполяции в выводе

print(numbers) # [10, 2, 3, 4, 5]

for i in numbers:
    i *= 2
    print(i) # [20, 4, 6, 8, 10]
print(numbers) # [10, 2, 3, 4, 5]


colors = ['red', 'green', 'blue']

for e in colors:
    print(e) # red green blue

for e in colors:
    print(e * 2) # redred greengreen blueblue

colors.append('gray') # добавить в конец
print(colors == ['red', 'green', 'blue', 'gray']) # True
colors.remove('red') # del colors[0] удалить элемент 
print(colors)