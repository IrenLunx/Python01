# Проверить истинность утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат

x = int(input('Введите число: '))
y = int(input('Введите число: '))
z = int(input('Введите число: '))
if -(x + y + z) == -x * -y * -z:
    print(True)
else:
    print(False)