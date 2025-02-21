from tkinter import *
import tkinter as tk
from tkinter import ttk
from functools import partial

class App(tk.Tk):
    def show_message(self, entry_Kp):
        print("entry_Kp = ", entry_Kp.get())
        # label["text"] = entry.get() , entry_Kp.get()

    def __init__(self):
        super().__init__()
        entry_Kp = tk.Entry(self, width=5)
        entry_Kp.grid(padx=6, pady=6, row=0, column=1) # почему так я не понял, если grid писать сразу после объявления то будет None и не получится
        print(entry_Kp)
        btn = tk.Button(self, text="Вывести", bg="yellow", command=partial(self.show_message, entry_Kp)).grid(row=2, column=1)
        #btn.pack(padx=6, pady=6)

if __name__ == "__main__":
    app = App()
    app.title("Интерфейс пользователя печки")
    app.mainloop()