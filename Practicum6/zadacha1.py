# [2, 2, 6, 7, 9, 1, 1] -> [6]

n = [2, 2, 6, 7, 9, 1, 1]
newList = [i for i in n if n.count(i) == 1]
print(newList)

n = [2, 2, 6, 7, 9, 1, 1]
res = list(filter(lambda x: n.count(x) == 1, n))
print(res)