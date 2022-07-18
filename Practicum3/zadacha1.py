# list() - список: изменяемый, индексируемый
# tuple() - кортеж: неизменяемый, индексируемый
# set() - множество: коллекция уникальных элементов, изменяемый, неиндексируемый, неупорядоченный
# dict() - словарь: изменяемый, индексируемый по ключу, ключ должен быть неизменяемым, нр, кортеж

my_tuple = tuple([1, 2, 3])
my_tuple = (1, 2, 3)
my_tuple = 1, 2, 3
my_tuple = 1,
a = [10, 9]
my_tuple = tuple(a)
print(my_tuple)

my_set = set()
my_set = {4, 7, 8} # пустыми скобками не создать
for i in my_set:
    print(i)

a = [1, 7, 9, 9 , 7]
a = set(a)
a = list(a)
print(a)

my_dict = dict()
my_dict = {
    ('20.12.1990', 'Vasya'): 'stul',
    753: 'stol'
}
my_dict[523] = 'shkaf'
print(my_dict)

for key in my_dict.values(): # .items() выведет ключ + значение
    print(key) # print(my_dict[key])

for key, val in my_dict.items():
    print(f'{key} - {val}')