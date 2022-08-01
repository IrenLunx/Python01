from HomeWork7.logger import line_by_line, search_by_name, to_the_column

def chooseUsers():
    print('Добро пожаловать в телефонный справочник Захолустья!\nЧто вы хотели бы сделать?\n')
    print('Для просмотра всех контактов построчно напишите "1"')
    print('Для просмотра всех контактов в столбец напишите "2"')
    print('Для поиска контакта по имени напишите "3"')
    print('Для добавления контакта напишите "4"')
    print('Для удаления контакта напишите "5"\n')
    checkChoose = False
    while not checkChoose:
        try:
            data = int(input('Ввод: '))
            checkChoose = True if 0 < data < 6 else print('Такого варианта нет!')
        except: print('Повторите ваш выбор: ')
    match data:
        case 1:
            line_by_line()
        case 2:
            to_the_column()
        case 3:
            name = input('Введите имя: ')
            search_by_name(name)
        case 4:
            
        case 5:
