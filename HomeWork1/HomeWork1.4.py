# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

a = int(input('Введите номер четверти прямоугольной системы координат: '))

if a == 1:
    print(f'Допустимые значения координат для точек {a} четверти: х > 0, у > 0')
elif a == 2:
    print(f'Допустимые значения координат для точек {a} четверти: x < 0, y > 0')  
elif a == 3:
    print(f'Допустимые значения координат для точек {a} четверти: x < 0, y < 0')   
elif a == 4:
    print(f'Допустимые значения координат для точек {a} четверти: x > 0, y < 0')   
else:
    print('Такой четверти не существует!')
    