from tkinter import *
import tkinter as tk
from tkinter.ttk import Checkbutton
from tkinter import messagebox


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        # tk.title("Интерфейс пользователя печки")

        opts = {'padx': 5, 'pady': 5, 'sticky': 'nswe'}

        group_1_t = tk.LabelFrame(self, padx=15, pady=10, text="COM-порт")
        group_1_t.grid(padx=10, pady=5, row=1, column=1)
        tk.Label(group_1_t, text="COM-порт:").grid(row=1)
        tk.Button(group_1_t, text="Выбрать").grid(row=1, column=2, sticky=tk.W)
        tk.Button(group_1_t, text="Подтвердить", bg="yellow").grid(row=2, column=1, columnspan=2)

        group_2_t = tk.LabelFrame(self, padx=15, pady=10, text="Коэффициенты ПИД")
        group_2_t.grid(padx=10, pady=5, row=2, column=1)
        tk.Label(group_2_t, text="По умалчанию: Kp = 3; Ki = 2; Kd = 1.").grid(row=1, column=1, columnspan=6)
        tk.Label(group_2_t, text="Kp:").grid(row=2, column=1)
        tk.Label(group_2_t, text="Ki:").grid(row=2, column=3)
        tk.Label(group_2_t, text="Kd:").grid(row=2, column=5)
        tk.Entry(group_2_t, width=5).grid(row=2, column=2, **opts)
        tk.Entry(group_2_t, width=5).grid(row=2, column=4, sticky=tk.W)
        tk.Entry(group_2_t, width=5).grid(row=2, column=6, sticky=tk.W)
        tk.Button(group_2_t, text="Изменить", bg="yellow").grid(row=3, column=6)

        group_3_t = tk.LabelFrame(self, padx=15, pady=10, text="Управление по сценарию")
        group_3_t.grid(padx=10, pady=5, row=3, column=1)
        tk.Label(group_3_t, text="Сценарий:").grid(row=1, column=1)
        tk.Button(group_3_t, text="Выбрать").grid(row=1, column=2, sticky=tk.W)
        tk.Label(group_3_t, text="Адрес файла:").grid(row=2, column=1)
        tk.Entry(group_3_t).grid(row=2, column=2, sticky=tk.W)
        tk.Button(group_3_t, text="Запустить\n сценарий", bg="Green").grid(row=3, column=1)
        tk.Button(group_3_t, text="Приостановить\n сценарий", bg="Red").grid(row=3, column=2)

        group_4_t = tk.LabelFrame(self, padx=15, pady=10, text="Ручное управление")
        group_4_t.grid(padx=10, pady=5, row=4, column=1)
        tk.Label(group_4_t, text="T_max").grid(row=1, column=1)
        tk.Label(group_4_t, text="ΔT").grid(row=1, column=3)
        tk.Label(group_4_t, text="Δt").grid(row=1, column=5)
        tk.Entry(group_4_t, width=5).grid(row=1, column=2, sticky=tk.W)
        tk.Entry(group_4_t, width=5).grid(row=1, column=4, sticky=tk.W)
        tk.Entry(group_4_t, width=5).grid(row=1, column=6, sticky=tk.W)
        tk.Label(group_4_t, text="<...>n").grid(row=2, column=1)
        tk.Label(group_4_t, text="Δt_R&T").grid(row=2, column=3)
        tk.Entry(group_4_t, width=5).grid(row=2, column=2, sticky=tk.W)
        tk.Entry(group_4_t, width=5).grid(row=2, column=4, sticky=tk.W)
        #tk.Button(group_4_t, text="Старт", bg="yellow").grid(row=3, column=6)
        tk.Button(group_4_t, text="Запустить", bg="Green").grid(row=3, column=1, columnspan=2)
        tk.Button(group_4_t, text="Приостановить", bg="Red").grid(row=3, column=4, columnspan=3)
        # <...>n -- к-во съемок\n для усреднения
        # <...>n -- периодичность\n съемки R и T

        group_1_r = tk.LabelFrame(self, padx=15, pady=10, text="Подключенные сенсоры и термопары")
        group_1_r.grid(padx=10, pady=5, row=1, column=2)
        chk_state_R = dict()
        chk_R = dict()
        for i in range(1, 17):
            Label(group_1_r, text="R%i" % i).grid(row=1, column=i)
            chk_state_R[i] = BooleanVar()
            chk_state_R[i].set(False)
            chk_R[i] = Checkbutton(group_1_r, var=chk_state_R[i]).grid(row=2, column=i)
            chk_state_R = dict()
            chk_R = dict()
            for i in range(1, 17):
                Label(group_1_r, text="R%i" % i).grid(row=1, column=i)
                chk_state_R[i] = BooleanVar()
                chk_state_R[i].set(False)
                chk_R[i] = Checkbutton(group_1_r, var=chk_state_R[i]).grid(row=2, column=i)
            chk_state_T = dict()
            chk_T = dict()
            for i in range(1, 10):
                Label(group_1_r, text="T%i" % i).grid(row=3, column=i)
                chk_state_T[i] = BooleanVar()
                chk_state_T[i].set(False)
                chk_T[i] = Checkbutton(group_1_r, var=chk_state_T[i]).grid(row=4, column=i)
            tk.Button(group_1_r, text="Подтвердить", bg="yellow").grid(row=3, column=13, rowspan=2, columnspan=4)


        group_2_r = tk.LabelFrame(self, padx=15, pady=10, text="График R(T)")
        group_2_r.grid(padx=10, pady=5, row=2, column=2)
        tk.Label(group_2_r, text="Пока пусто").grid(row=0)

        group_3_r = tk.LabelFrame(self, padx=15, pady=10, text="Данные с сенсоров и термопар")
        group_3_r.grid(padx=10, pady=5, row=3, column=2)
        tk.Label(group_3_r, text="R1").grid(row=0, column=1)
        tk.Label(group_3_r, text="R2").grid(row=0, column=3)
        tk.Label(group_3_r, text="R3").grid(row=2, column=1)
        tk.Label(group_3_r, text="R4").grid(row=2, column=3)
        tk.Label(group_3_r, text="T1").grid(row=1, column=2)


if __name__ == "__main__":
    app = App()
    app.mainloop()


'''
from tkinter import *
from tkinter import ttk

# настройка окна
root = Tk()
root.title("Интерфейс пользователя печки")
root.geometry("800x600")
# root.config(background = "Light Grey")

#Изображение меток, книпок
common_label_ui_params = {"font": ('Comic Sans MS', 12, 'bold'), "bd": 10}
common_grid_ui_params = dict(padx=30, pady=5)

Label_quit = Label(root, text = 'Quit', **common_label_ui_params)
Label_quit.pack()

root.mainloop()

'''

'''
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
window = tkinter.Tk()

Label_quit = Label(root, text = "quit", bg = "white", fg = "black", font = ("Arial", 30))
'''
