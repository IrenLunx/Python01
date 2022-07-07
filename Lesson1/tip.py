# типы данных и переменные
# int, float, boolean, str, list, None

value = None
a = 123
b = 1.23
# print(a)
# print(b)
print(type(a))
print(type(b))

value = 123567
print(type(value))


s = 'hello world'
print(s)

s = 'hello "world'
print(s)

s = "hello 'world"
print(s)

s = 'hello \'world'
print(s)

s = 'hello \nworld'
print(s)


print(a, '-', b, '-', s)
print('{} - {} - {}'.format(a, b, s))
print('{1} - {2} - {0}'.format(a, b, s))
print(f'{a} - {b} - {s}')


f = True
print(f)


list = []
print(list)

list = [1, 3, 5]
print(list)

list = ['1', '3', '5', 'hello']
print(list)


print('Введите a')
a = int(input())
print('Введите b')
b = int(input())
print(a + b)



