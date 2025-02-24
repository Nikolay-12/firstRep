from tkinter import *
import tkinter as tk
from tkinter import filedialog
from tkinter.ttk import Checkbutton
from tkinter.messagebox import showerror, showwarning, showinfo
from functools import partial
import serial
import serial.tools.list_ports

class App(tk.Tk):
    def is_it_float(self, newval):
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

    def selected_COM_port(self, List, connected):
        select = list(List.curselection())
        if len(select) != 0:
            global port
            port = connected[int(select[0])]
            print("Успешно выбран порт", port)
        else:
            showerror(title="Ошибка", message="Порт не выбран!")
            print("Порт не выбран")
    def coefficients_info(self, Kp, Ki, Kd, default_Kp, default_Ki, default_Kd):
        if (Kp.get() == 0 or Ki.get() == 0 or Kd.get() == 0):
            showinfo(title="Внимание",
                     message="Некоторые коэффициенты ПИД-регулятора не заданы, при работе будут использованы значения, заданные по умалчанию")
        print("Введенные коэффициенты: entry_Kp =", Kp.get(), "; entry_Ki =", Ki.get(), "; entry_Kd =", Kd.get())
        if (Kp.get() == 0): Kp.set(default_Kp)
        if (Ki.get() == 0): Ki.set(default_Ki)
        if (Kd.get() == 0): Kd.set(default_Kd)
        print("Коэффициенты для ПИД-регулятора: entry_Kp =", Kp.get(), "; entry_Ki =", Ki.get(), "; entry_Kd =", Kd.get())

    def manual_mode_info(self, entry_T_max, entry_ΔT, entry_Δt, entry_averaging, entry_Δt_R_T):
        print("entry_T_max =", entry_T_max.get(), "; entry_ΔT =", entry_ΔT.get(), "; entry_Δt =", entry_Δt.get(),
              "; <...>n =", entry_averaging.get(), "; Δt_R&T =", entry_Δt_R_T.get())
    def choose_mode_file(self,  entry_file_address):
        file_path = filedialog.askopenfilename()
        entry_file_address.set(file_path)
        print("Был выбран файл:", file_path)
    def run_mode_file(self,  entry_file_address, line_counter):
        file_path = entry_file_address.get()
        f = open(file_path, 'r', encoding='cp1252')
        command_line = ''
        value = line_counter.get()
       # line_counter = 0
        for line in f:
            command_line += line.strip() + ' '
            #line_counter+=1
            value+=1
        f.close()
        line_counter.set(value)
        print("Данные из файла", file_path, ": ", command_line, "\nКоличество команд:", line_counter.get())
    def stop_mode_file(self):
        print("Функция пока не готова")
    def input_data(selfport, port, Kp, Ki, Kd, entry_file_address):
        print("Выбранный порт:", port, "; Коэффициенты ПИД:", Kp.get(), Ki.get(), Kd.get(),
              "Режим работы (сценарий-0/ручной-1):", "Адрес файла-сценария:", entry_file_address.get())
    def save_data(self):
        print("Функция пока не готова")

    def __init__(self):
        super().__init__()

        check = (self.register(self.is_it_float), "%P")

        opts = {'padx': 5, 'pady': 5, 'sticky': 'nswe'}
        #common_entry_ui_params = {'padx': 5, 'pady': 5, 'sticky': 'nswe', 'validate': key, 'validatecommand': check}

        port_list = serial.tools.list_ports.comports()
        connected = []
        for element in port_list:
            connected.append(element.device)
        print("connected COM ports: " + str(connected))
        port = ''

        group_1_t = tk.LabelFrame(self, padx=15, pady=10, text="COM-порт")
        group_1_t.grid(padx=10, pady=5, row=1, column=1, sticky=tk.NSEW)
        tk.Label(group_1_t, text="COM-порт:").grid(row=1)
        List = tk.Listbox(group_1_t, width=20, height=2, selectmode='SINGLE')
        for i in range(len(connected)):
            List.insert(tk.END, connected[i])
        List.grid(row=1, column=2, sticky=tk.W)
        tk.Button(group_1_t, text="Подтвердить", bg="yellow", command=partial(self.selected_COM_port, List, connected)).grid(row=2, column=1, columnspan=2)
        # print(port)

        default_Kp, default_Ki, default_Kd = 3, 2, 1
        Kp, Ki, Kd = DoubleVar(value=default_Kp), DoubleVar(value=default_Ki), DoubleVar(value=default_Kd)
        group_2_t = tk.LabelFrame(self, padx=15, pady=10, text="Коэффициенты ПИД")
        group_2_t.grid(padx=10, pady=5, row=2, column=1, sticky=tk.NSEW)
        tk.Label(group_2_t, text="По умалчанию: Kp = 3; Ki = 2; Kd = 1.").grid(row=1, column=1, columnspan=6)
        tk.Label(group_2_t, text="Kp:").grid(row=2, column=1)
        tk.Label(group_2_t, text="Ki:").grid(row=2, column=3)
        tk.Label(group_2_t, text="Kd:").grid(row=2, column=5)
        entry_Kp = tk.Entry(group_2_t, validate="key", validatecommand=check, textvariable=Kp, width=5)
        entry_Kp.grid(row=2, column=2, sticky=tk.W)
        entry_Ki = tk.Entry(group_2_t, validate="key", validatecommand=check, textvariable=Ki, width=5)
        entry_Ki.grid(row=2, column=4, sticky=tk.W)
        entry_Kd = tk.Entry(group_2_t, validate="key", validatecommand=check, textvariable=Kd, width=5)
        entry_Kd.grid(row=2, column=6, sticky=tk.W)
        tk.Button(group_2_t, text="Изменить", bg="yellow",
                  command=partial(self.coefficients_info, Kp, Ki, Kd, default_Kp, default_Ki, default_Kd)).grid(row=3, column=6)

        group_3_t = tk.LabelFrame(self, padx=15, pady=10, text="Управление по сценарию")
        group_3_t.grid(padx=10, pady=5, row=3, column=1, sticky=tk.NSEW)
        tk.Label(group_3_t, text="Сценарий:").grid(row=1, column=1)
        entry_file_address = StringVar(value='')
        #line_counter = 0
        line_counter = IntVar(value=0)
        tk.Button(group_3_t, text="Выбрать", command=partial(self.choose_mode_file, entry_file_address)).grid(row=1, column=2, sticky=tk.W)
        tk.Label(group_3_t, text="Адрес файла:").grid(row=2, column=1)
        tk.Entry(group_3_t, state='disabled', textvariable=entry_file_address).grid(row=2, column=2) # , sticky=tk.NSEW
        tk.Button(group_3_t, text="Запустить\n сценарий", bg="Green", command=partial(self.run_mode_file, entry_file_address, line_counter)).grid(row=3, column=1)
        tk.Button(group_3_t, text="Приостановить\n сценарий", bg="Red", command=self.stop_mode_file).grid(row=3, column=2)
        print(line_counter.get())

        group_4_t = tk.LabelFrame(self, padx=15, pady=10, text="Ручное управление")
        group_4_t.grid(padx=10, pady=5, row=4, column=1, sticky=tk.NSEW)
        tk.Label(group_4_t, text="T_max").grid(row=1, column=1)
        tk.Label(group_4_t, text="ΔT").grid(row=1, column=3)
        tk.Label(group_4_t, text="Δt").grid(row=1, column=5)
        entry_T_max = tk.Entry(group_4_t, validate="key", validatecommand=check, width=5)
        entry_T_max.grid(row=1, column=2, sticky=tk.W)
        entry_ΔT = tk.Entry(group_4_t, validate="key", validatecommand=check, width=5)
        entry_ΔT.grid(row=1, column=4, sticky=tk.W)
        entry_Δt = tk.Entry(group_4_t, validate="key", validatecommand=check, width=5)
        entry_Δt.grid(row=1, column=6, sticky=tk.W)
        tk.Label(group_4_t, text="<...>n").grid(row=2, column=1)
        tk.Label(group_4_t, text="Δt_R&T").grid(row=2, column=3)
        entry_averaging = tk.Entry(group_4_t, validate="key", validatecommand=check, width=5)
        entry_averaging.grid(row=2, column=2, sticky=tk.W)
        entry_Δt_R_T = tk.Entry(group_4_t, validate="key", validatecommand=check, width=5)
        entry_Δt_R_T.grid(row=2, column=4, sticky=tk.W)
        tk.Button(group_4_t, text="Запустить", bg="Green",command=partial(self.manual_mode_info, entry_T_max, entry_ΔT, entry_Δt, entry_averaging, entry_Δt_R_T)).grid(row=3, column=1, columnspan=2)
        tk.Button(group_4_t, text="Приостановить", bg="Red").grid(row=3, column=4, columnspan=3)
        # <...>n -- к-во съемок\n для усреднения
        # Δt_R&T -- периодичность\n съемки R и T

        group_1_r = tk.LabelFrame(self, padx=15, pady=10, text="Подключенные сенсоры и термопары")
        group_1_r.grid(padx=10, pady=5, row=1, column=2, sticky=tk.NSEW)
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
        group_2_r.grid(padx=10, pady=5, row=2, column=2, sticky=tk.NSEW)
        tk.Label(group_2_r, text="Пока пусто").grid(row=0)

        group_3_r = tk.LabelFrame(self, padx=15, pady=10, text="Данные с сенсоров и термопар")
        group_3_r.grid(padx=10, pady=5, row=3, column=2, sticky=tk.NSEW)
        tk.Label(group_3_r, text="R1").grid(row=0, column=1)
        tk.Label(group_3_r, text="R2").grid(row=0, column=3)
        tk.Label(group_3_r, text="R3").grid(row=2, column=1)
        tk.Label(group_3_r, text="R4").grid(row=2, column=3)
        tk.Label(group_3_r, text="T1").grid(row=1, column=2)

        group_4_r = tk.LabelFrame(self, padx=15, pady=10, text="Дополнительные возможности")
        group_4_r.grid(padx=10, pady=5, row=4, column=2, sticky=tk.NSEW)
        tk.Label(group_4_r, text="Введенные данные:").grid(row=1, column=1)
        tk.Button(group_4_r, text="Получить",
                  command=partial(self.input_data, port, Kp, Ki, Kd, entry_file_address)).grid(row=1, column=2)
        tk.Label(group_4_r, text="Сохранение данных:").grid(row=1, column=1)
        tk.Button(group_4_r, text="Сохранить", command=self.save_data).grid(row=1, column=2)


if __name__ == "__main__":
    app = App()
    app.title("Интерфейс пользователя печки")
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
