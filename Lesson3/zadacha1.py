# В файле хранятся числа, нужно выбрать четные и составить список пар (число, квадат числа)
# Пример: 1 2 3 5 8 15 23 38
# Получится: [(2, 4), (8, 64), (38, 1444)]

path = 'Lesson3/zadacha1.txt'
with open(path, 'r') as f:
    data = f.readline().split(' ')
    data = [(int(i), int(i)**2) for i in data if int(i) % 2 == 0]
    print(data)

