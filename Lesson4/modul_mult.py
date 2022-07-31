x = 0
y = 0
def init(a, b):
    global x # без этого не увидит значения новые
    global y
    x = a
    y = b

def mult():
    return x * y