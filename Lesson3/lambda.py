def f(x):
    x**2
print(type(f))

#
def h(x):
    return x**2
print(h(2))

g = h # Присвоение функции переменной
print(h(1))
print(g(1))

#
def calc(x):
    return x*10

def math(op, x): # Функция, принимающая на вход функцию и значение
    print(op(x))

math(calc, 10)

#
def sum(x, y):
    return x+y

def mult(x, y):
    return x*y

def calc1(op, a, b): # Для двух аргументов функции
    return op(a, b)

print(calc1(mult, 2, 3))
print(calc1(sum, 2, 3))

#
def sum2(x, y):
    return x+y

p = lambda x, y: x + y # Та же ^ функция, только как лямбда
print(calc1(p, 2, 3))

print(calc1(lambda x, y: x + y, 4, 5)) # Или сразу передавать лямбду как аргумент

#
