from data import graph, graph2, people

def clicClac():
    print('Для добавления посещения урока учеником нажмите 1:')
    print('Для просмотра журнала посещений кабинета нажмите 2:')
    print('Для просмотра номеров/адресов учеников/родителей нажмите 3:')
    data = int(input('Введите цифру:'))
    match data:
        case 1:
            graph()
        case 2:
            graph2()
        case 3:
            people()