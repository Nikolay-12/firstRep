from tkinter import *
import tkinter as tk
from tkinter import filedialog
from tkinter.ttk import Checkbutton, Combobox
from tkinter.messagebox import showerror, showwarning, showinfo
from functools import partial
import serial
import serial.tools.list_ports
import matplotlib.pyplot as plt
import matplotlib.figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import numpy as np

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

    def COM_port_setting(self, List, connected, combo):
        select = list(List.curselection())
        if len(select) != 0:
            global port
            port = connected[int(select[0])]
            #used_port = port
            print("Успешно выбран порт", port)
        else:
            showerror(title="Ошибка", message="Порт не выбран!")
            print("Порт не выбран")
        print("Baud rate:", combo.get())
    def coefficients_info(self, Kp, Ki, Kd, default_Kp, default_Ki, default_Kd):
        if (Kp.get() == 0 or Ki.get() == 0 or Kd.get() == 0):
            showinfo(title="Внимание",
                     message="Некоторые коэффициенты ПИД-регулятора не заданы, при работе будут использованы значения, заданные по умалчанию")
        print("Введенные коэффициенты: Kp =", Kp.get(), "; Ki =", Ki.get(), "; Kd =", Kd.get())
        if (Kp.get() == 0): Kp.set(default_Kp)
        if (Ki.get() == 0): Ki.set(default_Ki)
        if (Kd.get() == 0): Kd.set(default_Kd)
        print("Коэффициенты для ПИД-регулятора: Kp =", Kp.get(), "; Ki =", Ki.get(), "; Kd =", Kd.get())
    def manual_mode_info(self, entry_T_max, entry_ΔT, entry_Δt, entry_averaging, entry_Δt_R_T):
        print("T_max =", entry_T_max.get(), "; ΔT =", entry_ΔT.get(), "; Δt =", entry_Δt.get(),
              "; <...>n =", entry_averaging.get(), "; Δt_R&T =", entry_Δt_R_T.get())
    def choose_mode_file(self,  entry_file_address):
        file_path = filedialog.askopenfilename()
        entry_file_address.set(file_path)
        print("Был выбран файл:", file_path)
    def devices_used(self, chk_state_R, chk_state_T):
        global devices_connected
        devices_connected = []
        for i in range(1, 17):
            if (chk_state_R[i].get() == 1):
                devices_connected.append("R%i"%i)
        for i in range(1, 10):
            if (chk_state_T[i].get() == 1):
                devices_connected.append("T%i"%i)
        print("Подключенные устройства:", devices_connected)
    def run_mode_file(self,  entry_file_address, line_counter):
        file_path = entry_file_address.get()
        f = open(file_path, 'r', encoding='cp1252')
        command_line = ''
        value = line_counter.get()
        value = 0
        for line in f:
            command_line += line.strip() + ' '
            value+=1
        f.close()
        line_counter.set(value)
        print("Данные из файла", file_path, ": ", command_line, "\nКоличество команд:", line_counter.get())
    def stop_mode_file(self):
        print("Функция пока не готова")
    def input_data(self, combo, Kp, Ki, Kd, entry_file_address): #port, , devices_connected
        try:
            print("Выбранный порт:", port, "; Baud rate:", combo.get(), "; Подключенные устройства:", devices_connected,
                  ";\nКоэффициенты ПИД:", Kp.get(), Ki.get(), Kd.get(), "; Режим работы (сценарий-0/ручной-1):",
                  ";\nАдрес файла-сценария:", entry_file_address.get())
        except NameError:
            port = "нету его"
            devices_connected = ["неа"]
            print("Выбранный порт:", port, "; Baud rate:", combo.get(), "; Подключенные устройства:", devices_connected,
                  ";\nКоэффициенты ПИД:", Kp.get(), Ki.get(), Kd.get(), "; Режим работы (сценарий-0/ручной-1):",
                  ";\nАдрес файла-сценария:", entry_file_address.get())
    def save_data(self, combo, Kp, Ki, Kd, entry_file_address):
        devices_connected = []
        port= ''
        if (len(devices_connected) == 0):
            showinfo(title="Внимание", message="Не выбраны подключенные устройства! Запустить измерение не получится.")
        global saved_file_path
        saved_file_path = filedialog.asksaveasfilename(initialfile="Untitled.txt", filetypes=[("Text files", "*.txt")])
        if saved_file_path:
            f = open(saved_file_path, 'w+')
            f.writelines(f'Выбранный порт: {port}; Baud rate: {combo.get()}; Подключенные устройства: {devices_connected}\n'
                         f'Коэффициенты ПИД: {Kp.get()} {Ki.get()} {Kd.get()}; Режим работы (сценарий-0/ручной-1): ;\n'
                         f'Адрес файла-сценария: {entry_file_address.get()}')
            #print(f"Saving preferences to {saved_file_path}")
            f.close()
        else:
            print("File save operation cancelled.")

    def __init__(self):
        super().__init__()

        check = (self.register(self.is_it_float), "%P")
        #devices_connected = []
        opts = {'padx': 5, 'pady': 5, 'sticky': 'nswe'}
        #common_entry_ui_params = {'padx': 5, 'pady': 5, 'sticky': 'nswe', 'validate': key, 'validatecommand': check}

        port_list = serial.tools.list_ports.comports()
        connected = []
        for element in port_list:
            connected.append(element.device)
        print("connected COM ports: " + str(connected))
        #port = None

        group_1_t = tk.LabelFrame(self, padx=15, pady=10, text="COM-порт")
        group_1_t.grid(padx=10, pady=5, row=1, column=1, sticky=tk.NSEW)
        tk.Label(group_1_t, text="COM-порт:").grid(row=1, column=1)
        List = tk.Listbox(group_1_t, width=20, height=2, selectmode='SINGLE')
        for i in range(len(connected)):
            List.insert(tk.END, connected[i])
        List.grid(row=1, column=2, sticky=tk.W)
        tk.Label(group_1_t, text="Скорость обмена\n данных по порту:").grid(row=2, column=1)
        combo = Combobox(group_1_t, width=15)
        combo['values'] = (4800, 9600, 19200, 38400)
        combo.current(1)
        combo.grid(row=2, column=2)
        tk.Button(group_1_t, text="Подтвердить", bg="yellow",
                  command=partial(self.COM_port_setting, List, connected, combo)).grid(row=3, column=1, columnspan=2)

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

        group_5_t = tk.LabelFrame(self, padx=15, pady=10, text="Дополнительные возможности")
        group_5_t.grid(padx=10, pady=5, row=5, column=1, sticky=tk.NSEW)
        tk.Label(group_5_t, text="Введенные данные:").grid(row=1, column=1)
        tk.Button(group_5_t, text="Получить",
                  command=partial(self.input_data, combo, Kp, Ki, Kd, entry_file_address)).grid(row=1, column=2) #port,, devices_connected
        tk.Label(group_5_t, text="Сохранение данных:").grid(row=2, column=1)
        tk.Button(group_5_t, text="Сохранить", command=partial(self.save_data, combo, Kp, Ki, Kd, entry_file_address)).grid(row=2, column=2)

        group_1_r = tk.LabelFrame(self, padx=15, pady=10, text="Подключенные сенсоры и термопары")
        group_1_r.grid(padx=10, pady=5, row=1, column=2, sticky=tk.NSEW)
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
            chk_state_T[i] = BooleanVar(value=False)
            chk_T[i] = Checkbutton(group_1_r, var=chk_state_T[i]).grid(row=4, column=i)
        tk.Button(group_1_r, text="Подтвердить", bg="yellow", command=partial(self.devices_used, chk_state_R, chk_state_T)).grid(row=3, column=13, rowspan=2, columnspan=4)

        group_2_r = tk.LabelFrame(self, padx=15, pady=10, text="График R(T)")
        group_2_r.grid(padx=10, pady=5, row=2, column=2, rowspan=3, sticky=tk.NSEW)
        #tk.Label(group_2_r, text="Пока пусто").grid(row=0)
        fig = matplotlib.figure.Figure(figsize=(4,3), dpi=100)
        ax = fig.add_subplot(1,1,1)
        canvas = FigureCanvasTkAgg(fig, master=group_2_r)
        canvas.get_tk_widget().grid(row=1)
        toolbar = NavigationToolbar2Tk(canvas, group_2_r, pack_toolbar=False)
        toolbar.update()
        toolbar.grid(row=2, sticky=tk.W)

        '''
        group_3_r = tk.LabelFrame(self, padx=15, pady=10, text="Данные с сенсоров и термопар")
        group_3_r.grid(padx=10, pady=5, row=5, column=2, sticky=tk.NSEW)
        tk.Label(group_3_r, text="R1").grid(row=0, column=1)
        tk.Label(group_3_r, text="R2").grid(row=0, column=3)
        tk.Label(group_3_r, text="R3").grid(row=2, column=1)
        tk.Label(group_3_r, text="R4").grid(row=2, column=3)
        tk.Label(group_3_r, text="T1").grid(row=1, column=2)
        '''

if __name__ == "__main__":
    app = App()
    app.title("Интерфейс пользователя печки")
    app.mainloop()