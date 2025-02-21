from tkinter import *
from tkinter import ttk

def show_message():
    print(VarEnt.get())
    #label["text"] = entry.get()

def is_it_float(newval):
    valid_symbols = list("-,.0123456789")
    for symb in newval:
        if symb not in valid_symbols:
            return False
    if newval == '-' or newval == '':
        return True
    else:
        try:
            float(newval)
        except:
            return False
    return True

'''
result=  re.match("^\+{0,1}\d{0,11}$", newval) is not None
    if not result and len(newval) <= 12:
        errmsg.set("Число должно быть десятичной дробью")
    else:
        errmsg.set("")
    return result
'''


root = Tk()
root.title("Интерфейс пользователя печки")
root.geometry("200x200")

check = (root.register(is_it_float), "%P")

VarEnt = Entry(root, validate="key",validatecommand=check, width=5)
VarEnt.pack()
btn = Button(text="Click", command=show_message)
btn.pack(padx=6, pady=6)

root.mainloop()