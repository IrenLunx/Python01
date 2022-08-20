class DataBase:
    def __init__(self, path='data_base\data\phone_book.txt'):
        self.path = path

    def lookContacts(self):
        with open(self.path, 'r', encoding = 'utf-8') as file: 
            data = file.readlines()
            res = ''
            for i in data:
                res += f'{i}'
        return res

    def lookForName(self, name: str):
        with open(self.path, 'r', encoding = 'utf-8') as file: 
            data = file.readlines()
            res = ''
            for i in data:
                if name in i: 
                    res += f'{i}'
        return res

    def dellContact(self, name: str):
        with open(self.path, 'r', encoding = 'utf-8') as file:
            data = file.readlines()
        with open(self.path, 'w', encoding = 'utf-8') as file2:
            for i in data:
                if name.lower() not in i.lower(): file2.write(i)

    def addContact(self, name, number, commUs):
        name = input('Введите имя: ')
        number = input('Введите номер: ')
        commUs = input('Введите комментарий: ')
        newUs = f'{name} {number} {commUs}'
        with open(self.path, 'a', encoding = 'utf-8') as file:
            file.write(f'\n{newUs}')