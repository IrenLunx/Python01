# Задайте список. Напишите программу, которая определит, присутствуют ли в заданном списке строк некое число
# Пример:
# list_str = ['465jgjyy675', '556', '89', '56', 'ghj']
# find_str = 12



list_str = ['465jgjyy675', '556', '89', '56', 'ghj']
number = input('Введите число: ')
a = False
for i in list_str:
    if i.__contains__(number): # так просто найдет число, если нужна вся строка: number == i. функцию _contains_ можно заменить number in i
        a = True
        break
if a:
    print(f'{number} есть в {list_str}')
else:
    print(f'{number} нет в {list_str}')


