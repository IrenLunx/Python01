

text = 'съешь еще этих мягких французских булок'
print(len(text)) # количество символов (39)
print('еще' in text) # наличие подстроки в строке (True)
print(text.isdigit()) # все символы строки числа (False)
print(text.islower()) # все символы нижнего регистра (True)
print(text.replace('еще', 'ЕЩЕ')) # замена
print(text[0]) # с
print(text[1]) # ъ
print(text[len(text) - 1]) # к (если без -1 будет ошибка)
print(text[-5]) # б
print(text[:]) # print(text), то есть от 0 до последнего символа
print(text[:2]) # съ
print(text[len(text) - 2:]) # ок
print(text[2:9]) # ешь еще
print(text[6:-18]) # еще этих мягких
print(text[0 : len(text) : 6]) # сеикакл
print(text[::6]) # сеикакл



# help(text.istitle) справка 

for c in text:
    print(c)