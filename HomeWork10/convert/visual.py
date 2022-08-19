from tkinter import *
from tkinter.ttk import Combobox
from main import ConvertVal

def clicked():
    res = txt.get()
    res = float()
    match combo.get():
        case 'Доллары в рубли': convert_res(res, 1),
        case 'Рубли в доллары': convert_res(res, 2),
        case 'Евро в рубли': convert_res(res, 3),
        case 'Рубли в евро': convert_res(res, 4)

def convert_res(res, val):
    match val:
        case 1: 
            result = ConvertVal.Dollar_Rub()
            result *= res
            lbl4 = Label(root, text=f"{result}", font=("Arial Bold", 10))
            lbl4.grid(column=1, row=2)
        case 2:
            result = ConvertVal.Dollar_Rub()
            result = res / result
            lbl4 = Label(root, text=f"{result}", font=("Arial Bold", 10))
            lbl4.grid(column=1, row=2)
        case 3:
            result = ConvertVal.Eur_Rub()
            result *= res
            lbl4 = Label(root, text=f"{result}", font=("Arial Bold", 10))
            lbl4.grid(column=1, row=2)
        case 4:
            result = ConvertVal.Eur_Rub()
            result = res / result
            lbl4 = Label(root, text=f"{result}", font=("Arial Bold", 10))
            lbl4.grid(column=1, row=2)
            
root = Tk()
root.title("Конвертер валют")
root.geometry("500x200")
combo = Combobox(root) 
txt = Entry(root, width=10)

lbl = Label(root, text="Выберите вариант", font=("Arial Bold", 10))
lbl.grid(column=0, row=0) 

lbl2 = Label(root, text="Введите число", font=("Arial Bold", 10))
lbl2.grid(column=0, row=1)

lbl3 = Label(root, text="Результат:", font=("Arial Bold", 10))
lbl3.grid(column=0, row=2)

txt = Entry(root, width=20)  
txt.grid(column=1, row=1)

btn = Button(root, text="Конвертировать", command=clicked())  
btn.grid(column=2, row=1) 

combo['values'] = ('Доллары в рубли', 'Рубли в доллары', 'Евро в рубли', 'Рубли в евро')  
combo.current(0)
combo.grid(column=1, row=0) 

root.mainloop()  
 
