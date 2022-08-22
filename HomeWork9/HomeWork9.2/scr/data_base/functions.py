class DataBase:
    def __init__(self, path='data_base\data\phone_book.txt'):
        self.path = path

    contact = ''

    def addResult(self, mess: str):
        self.contact += f'{mess} '

    def addContact(self):
        with open(self.path, 'a', encoding = 'utf-8') as file:
            file.write(f'\n{self.contact}')

    def clearContact(self):
        self.contact = ''

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
            count = False
            for i in data:
                if name.lower() in i.lower(): 
                    count = True
                    break
            if count:
                with open(self.path, 'w', encoding = 'utf-8') as file2:
                    for i in data:
                        if name.lower() not in i.lower(): file2.write(i)
                return True
            else: return False