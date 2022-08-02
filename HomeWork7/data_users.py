from logger import addData, line_by_line, search_by_name, to_the_column, deleteData

def chooseUsers():
    print('Добро пожаловать в телефонный справочник Захолустья!\nЧто вы хотели бы сделать?\n')
    print('Для просмотра всех контактов построчно напишите "1"')
    print('Для просмотра всех контактов в столбец напишите "2"')
    print('Для поиска контакта по имени напишите "3"')
    print('Для удаления контакта напишите "4"')
    print('Для добавления контакта напишите "5"\n')
    checkChoose = False
    while not checkChoose:
        try:
            data = int(input('Ввод: '))
            checkChoose = True if 0 < data < 6 else print('Такого варианта нет!')
        except: print('Повторите ваш выбор: ')
    match data:
        case 1:
            line_by_line()
            print('Спасибо за использование нашего приложения! Все данные вы можете посмотреть в файле "scan.csv".')
        case 2:
            to_the_column()
            print('Спасибо за использование нашего приложения! Все данные вы можете посмотреть в файле "scan.csv".')
        case 3:
            name = input('Введите имя: ')
            search_by_name(name)
            print('Спасибо за использование нашего приложения! Все данные вы можете посмотреть в файле "scan.csv".')
        case 4:
            name = input('Введите имя контакта для удаления: ')
            deleteData(name)
            print('Спасибо за использование нашего приложения! Все данные вы можете посмотреть в файле "phone_book.txt".')
        case 5:
            name = input('Введите ФИ контакта для добавления: ')
            number = input('Введите номер контакта: ')
            commUs = input('Введите комментарий к номеру: ')
            addData(name, number, commUs)
            print('Спасибо за использование нашего приложения! Все данные вы можете посмотреть в файле "phone_book.txt".')
            