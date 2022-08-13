def lookContacts():
    path = 'HomeWork9/HomeWork9.1/phone_book.txt'
    with open(path, 'r', encoding = 'utf-8') as file: data = file.readlines()

    with open('scan.csv', 'w', encoding = 'utf-8') as file2:
        for i in data: file2.write(i)

def lookForName():
    name = input('Введите имя для поиска')
    path = 'HomeWork9/HomeWork9.1/phone_book.txt'
    with open(path, 'r', encoding = 'utf-8') as file: data = file.readlines()

    with open('scan.csv', 'w', encoding = 'utf-8') as file2:
        for i in data:
            if name.lower() in i.lower(): file2.write(i)

def dellContact():
    val = input('Введите имя для удаления')
    path = 'HomeWork9/HomeWork9.1/phone_book.txt'
    with open(path, 'r', encoding = 'utf-8') as file:
        data = file.readlines()
    with open(path, 'w', encoding = 'utf-8') as file2:
        for i in data:
            if val.lower() not in i.lower(): file2.write(i)

def addContact():
    name = input('Введите имя: ')
    number = input('Введите номер: ')
    commUs = input('Введите комментарий: ')
    path = 'HomeWork9/HomeWork9.1/phone_book.txt'
    newUs = f'{name} {number} {commUs}'
    with open(path, 'a', encoding = 'utf-8') as file:
        file.write(f'\n{newUs}')