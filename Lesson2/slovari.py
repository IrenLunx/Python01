# Словари - неупорядоченные коллекции произвольных объектов с доступом по ключу

dictionary = {}

# \ нужен, чтобы не писать все в одну строку
dictionary = \
    {
        'up': '^',
        'left': '<',
        'down': 'v',
        'right': '>'
    }
print(dictionary)
print(dictionary['left'])

for k in dictionary.keys(): # цикл для просмотра ключей 
    print(k)

for k in dictionary.values(): # цикл для просмотра значений
    print(k)

for k in dictionary: # цикл для прохода по словарю
    print(k)

for k in dictionary: # цикл для прохода по элементам словаря
    print(dictionary[k])

print(dictionary['up'])
dictionary['up'] = 'up' # замена элементов ключа
print(dictionary['up'])