# Сложить 2 числа

# a = 5
# b = 10
# f = lambda x, y: x + y
# result = f(a, b)
# print(result)
# _______________

x = 0
y = 0
def init(a, b):
    global x # без этого не увидит значения новые
    global y
    x = a
    y = b

# init(11, 22)
# print(x)
# print(y)

def sum():
    return x + y