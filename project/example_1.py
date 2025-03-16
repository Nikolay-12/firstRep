import tkinter as tk
from tkinter.ttk import Combobox
import serial
import serial.tools.list_ports


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.port = None
        self.button_pressed_times = 0

        port_list = serial.tools.list_ports.comports()
        connected = []
        for element in port_list:
            connected.append(element.device)


        tk.Label(self, text="COM-порт:").grid(row=1, column=1)
        tk.Button(self, text="Подтвердить", bg="yellow",
                  command=self.modify_comport_settings).grid(row=3, column=1, columnspan=2)

        self.comports_listbox = tk.Listbox(self, width=20, height=10, selectmode='MULTIPLE')
        for i in range(len(connected)):
            self.comports_listbox.insert(tk.END, connected[i])
        self.comports_listbox.grid(row=1, column=2, sticky=tk.W)


        self.baudrate_combobox = Combobox(self, width=15)
        self.baudrate_combobox['values'] = (4800, 9600, 19200, 38400)
        self.baudrate_combobox.current(1)
        self.baudrate_combobox.grid(row=2, column=2)



    def modify_comport_settings(self):
        selected_comport_idxes = self.comports_listbox.curselection()
        if len(selected_comport_idxes) > 0:
            self.port = self.comports_listbox.get(selected_comport_idxes[0])



if __name__ == "__main__":
    app = App()
    app.title("Интерфейс пользователя печки")
    app.mainloop()
