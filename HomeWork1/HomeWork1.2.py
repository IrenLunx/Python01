# Проверить истинность утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат

x = int(input('Введите число x: '))
y = int(input('Введите число y: '))
z = int(input('Введите число z: '))
if not (x or y or z) == (not x) and (not y) and (not z):
    print(True)
else:
    print(False)