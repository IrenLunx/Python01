# Дано число обозначающее день недели. Вывести его название и указать является ли он выходным.

a = int(input('Введите число от 1 до 7: '))
week = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']
if a in range(1, 8):
    print(week[a - 1])
    if a in range(1, 5):
        print(week[a - 1], '- будний день')
    else:
        print(week[a - 1], '- выходной день')
else:
    print('Такого дня недели нет!')