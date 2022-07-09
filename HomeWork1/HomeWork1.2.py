# Проверить истинность утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат

x = int(input('Введите число x: '))
y = int(input('Введите число y: '))
z = int(input('Введите число z: '))
if -(x + y + z) == -x * -y * -z:
    print(True)
else:
    print(False)