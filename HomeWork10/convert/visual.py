from tkinter import *
from tkinter.ttk import Combobox
from main import dollar_rub, eur_rub

def clicked(money, target, lbl_res: Label):
    res = 0
    match target:
        case 'Доллары в рубли': res = convert_res(money, 1)
        case 'Рубли в доллары': res = convert_res(money, 2)
        case 'Евро в рубли': res = convert_res(money, 3)
        case 'Рубли в евро': res = convert_res(money, 4)
    lbl_res.configure(text=f'{round(res, 3)}')

def convert_res(res, val):
    match val:
        case 1: 
            result = dollar_rub()
            result *= res
            return result
        case 2:
            result = dollar_rub()
            result = res / result
            return result
        case 3:
            result = eur_rub()
            result *= res
            return result
        case 4:
            result = eur_rub()
            result = res / result
            return result
            
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

lbl4 = Label(root, text='', font=("Arial Bold", 10))
lbl4.grid(column=1, row=2)

txt_money = Entry(root, width=20)  
txt_money.grid(column=1, row=1)

combo['values'] = ('Доллары в рубли', 'Рубли в доллары', 'Евро в рубли', 'Рубли в евро')  
combo.current(0)
combo.grid(column=1, row=0) 

btn = Button(root, text="Конвертировать", command=lambda: clicked(float(txt_money.get()), combo.get(), lbl4))
btn.grid(column=2, row=1) 

root.mainloop()  
 
