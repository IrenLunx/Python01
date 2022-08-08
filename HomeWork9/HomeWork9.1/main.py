import tkinter
import random2

def printList(newList: list):
    for i in newList: print(i)

def returnPoz(number: int, newList: list, count: str) -> list:
    if number == 1: newList[0][0] = count
    elif number == 2: newList[0][1] = count
    elif number == 3: newList[0][2] = count
    elif number == 4: newList[1][0] = count
    elif number == 5: newList[1][1] = count
    elif number == 6: newList[1][2] = count
    elif number == 7: newList[2][0] = count
    elif number == 8: newList[2][1] = count
    elif number == 9: newList[2][2] = count
    return newList

def trueFalseNull(newList: list, count: str):
    checkInput = False
    for i in range(len(newList)):
        for j in range(len(newList)):
            if newList[i][j] == count:
                checkInput = True
                break
    return checkInput

def trueFalseVal(number: int, newList: list):
    if number == 1: 
        if newList[0][0] == 'X' or newList[0][0] == '0': return False
        else: return True
    elif number == 2: 
        if newList[0][1] == 'X' or newList[0][1] == '0': return False
        else: return True
    elif number == 3:
        if newList[0][2] == 'X' or newList[0][2] == '0': return False
        else: return True
    elif number == 4: 
        if newList[1][0] == 'X' or newList[1][0] == '0': return False
        else: return True
    elif number == 5: 
        if newList[1][1] == 'X' or newList[1][1] == '0': return False
        else: return True
    elif number == 6: 
        if newList[1][2] == 'X' or newList[1][2] == '0': return False
        else: return True
    elif number == 7:
        if newList[2][0] == 'X' or newList[2][0] == '0': return False
        else: return True
    elif number == 8: 
        if newList[2][1] == 'X' or newList[2][1] == '0': return False
        else: return True
    elif number == 9: 
        if newList[2][2] == 'X' or newList[2][2] == '0': return False
        else: return True

def winGame(newList: list):
    if newList[0][0] == newList[1][1] == newList[2][2] != ' ': return True
    elif newList[0][2] == newList[1][1] == newList[2][0] != ' ': return True
    elif newList[0][0] == newList[0][1] == newList[0][2] != ' ': return True
    elif newList[1][0] == newList[1][1] == newList[1][2] != ' ': return True
    elif newList[2][0] == newList[2][1] == newList[2][2] != ' ': return True
    elif newList[0][0] == newList[1][0] == newList[2][0] != ' ': return True
    elif newList[0][1] == newList[1][1] == newList[2][1] != ' ': return True
    elif newList[0][2] == newList[1][2] == newList[2][2] != ' ': return True
    else: return False

newList = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
newList2 = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
print('Номера ячеек:')
printList(newList2)
print()
gamers = random2.randint(1, 2)

if gamers == 1: print('Первый ход ваш!')
else: print('Я хожу первым!')
print()
for i in range(len(newList)*2):
    if trueFalseNull(newList, ' '):
        if gamers == 1:
            checkInput = False
            while not checkInput:
                try:
                    printList(newList)
                    number = int(input('Введите номер свободной ячейки: '))
                    checkInput = True if trueFalseVal(number, newList) else print('Позиция занята!')
                except: print('Введите новую позицию: ')
            print()
            newList = returnPoz(number, newList, 'X')

            if winGame(newList) == True:
                printList(newList)
                print(f'Победил игрок №{gamers}!')
                break
            elif trueFalseNull(newList, ' '): gamers = 2
        if gamers == 2:
            checkInput = False
            while not checkInput:
                try:
                    printList(newList)
                    number = int(input('Я ввожу: '))
                    checkInput = True if trueFalseVal(number, newList) else print('Позиция занята!')
                except: print('Новая позиция: ')
            print()
            newList = returnPoz(number, newList, '0')

            if winGame(newList) == True:
                printList(newList)
                print(f'Я победил!')
                break
            elif trueFalseNull(newList, ' '): gamers = 1
    else: 
        printList(newList)
        print('Ничья!')
