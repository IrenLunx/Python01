# Логические операции
# and - и, or - или
# можно использовать несколько знаков неравенства: a = 5 > 10 > 11
# is, is not, in, not in

a = 5 > 4 and 8 < 10
print(a)


f = [1, 3, 4, 5]
print(not 2 in f)


is_odd = not f[0] % 2 # is_odd = f[0] % 2 == 0
print(is_odd)