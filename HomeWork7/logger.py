

def line_by_line():
    path = 'phone_book.txt'
    with open(path, 'r', encoding = 'utf-8') as file: data = file.readlines()

    with open('scan.csv', 'w', encoding = 'utf-8') as file2:
        for i in data: file2.write(i.replace(' ', ';'))

def to_the_column():
    path = 'phone_book.txt'
    with open(path, 'r', encoding = 'utf-8') as file: data = file.readlines()

    with open('scan.csv', 'w', encoding = 'utf-8') as file2:
        for i in data:
            file2.write(i.replace(' ', '\n'))
            file2.write('\n')

def search_by_name(name: str):
    path = 'phone_book.txt'
    with open(path, 'r', encoding = 'utf-8') as file: data = file.readlines()

    with open('scan.csv', 'w', encoding = 'utf-8') as file2:
        for i in data:
            if name.lower() in i.lower(): file2.write(i)

