# Функция enumerate() применяется к итерируемому объекту и возвращает новый итератор с кортежами из индекса и элементов входных данных

users = ['users1', 'users2', 'users3', 'users4', 'users5']
ids = [4, 5, 9, 14, 7]
data = list(enumerate(users))
print(data)