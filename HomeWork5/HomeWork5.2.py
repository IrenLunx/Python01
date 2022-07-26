# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, 
# чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота "интеллектом"

import random

def candyGame(gamers, n):
    print(f'Ход игрока №{gamers}!')
    print(f'Конфет осталось: {n}')

def winGamers(gamers, n):
    print(f'Победил игрок №{gamers}!')
    return n - 1

print('Условия игры: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.')
print('Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.') 
print('Все конфеты оппонента достаются сделавшему последний ход.')
print()
gamers = random.randint(1, 2)
print(f'Первый ход игрока №{gamers}!')
n = 2021
while n >= 0:
    checkInput = False
    if gamers == 1:
        candyGame(gamers, n)
        while not checkInput:
            try:
                number = int(input('Возьмите от 1 до 28 конфет: '))
                print(f'Игрок взял {number} конфет.')
                checkInput = True if 0 < number <= 28 else print('Вы вышли из диапазона!')
            except:
                print('Введите число от 1 до 28: ')
        n -= number
        if n == 0:
            n = winGamers(gamers, n)
        else:
            gamers = 2
        print()
    elif gamers == 2:
        candyGame(gamers, n)
        if n % 29 == 0:
            number2 = random.randint(1, 28)
        else:    
            number2 = n % 29
        print(f'Игрок взял {number2} конфет.')
        n -= number2
        if n == 0:
            n = winGamers(gamers, n)
        else:
            gamers = 1
    print()