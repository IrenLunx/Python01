import pandas as pd
from datetime import date, time, datetime

def graph():
    ID_stu = input('ID студента: ')
    ID_class = input('ID места в классе: ')
    dateNow = date.today()
    timeNow = datetime.now().time()
    newStr = f'{ID_stu},{ID_class},{str(dateNow)},{str(timeNow)}'

    path = 'graph.csv'
    with open(path, 'a', encoding = 'utf-8') as cl: 
        cl.write(newStr)
        cl.write('\n')
    
    graph = pd.read_csv('graph.csv')
    print(graph)

   

def graph2():
    table = pd.read_csv('students.csv')
    table2 = pd.read_csv('graph.csv')
    table3 = pd.read_csv('class.csv')

    result = table3.merge(table2).merge(table)
    print(result)

def people():
    table = pd.read_csv('people.csv')
    table2 = pd.read_csv('adress.csv')
    table3 = pd.read_csv('phone_numbers.csv')

    result = table3.merge(table).merge(table2)
    print(result)