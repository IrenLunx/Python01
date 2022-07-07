# if, else, elif

a = int(input('a = '))
b = int(input('b = '))
if a > b:
    print(a)
else:
    print(b)


username = input('Введите имя: ')
if username == 'Маша':
    print('Ура! Это же Маша!')
elif username == 'Марина':
    print('Ура! Это же Марина!')
elif username == 'Ильнар':
    print('Ура! Это же Ильнар!')
else:
    print('Привет, ', username)