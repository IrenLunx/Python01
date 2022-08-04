import pandas as pd

# table = pd.read_csv('HomeWork8/classAud.csv')
# table2 = pd.read_csv('HomeWork8/class.csv')
# print()
df = pd.concat(
    map(pd.read_csv, ['HomeWork8/people.csv', 'HomeWork8/students.csv']), ignore_index=True)
print(df)

# def classSt():
#     сlassAud = {}
#     path = 'HomeWork8/class.csv'
#     path2 = 'HomeWork8/classAud.csv'
#     with open(path, 'r', encoding = 'utf-8') as cl:
#         data = cl.readlines()
#     with open(path2, 'r', encoding = 'utf-8') as cl2:
#         data2 = cl2.readlines()
#         for i in data2:
#             сlassAud[i] = data
#     print(сlassAud)
# classSt()