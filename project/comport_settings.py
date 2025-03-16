import tkinter as tk
import tkinter.ttk as ttk
from utils.comports import get_comports

class ComportException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class ComportSettings():
    def __init__(self, parent) -> None:
        self.parent = parent
        self._port = None
        self._baudrate = None

    def ui_draw(self):
        serial_settings_frame = tk.LabelFrame(self.parent, padx=15, pady=10, text="Настройки COM-порта")
        serial_settings_frame.grid(padx=10, pady=5, row=1, column=1, sticky=tk.NW)


        tk.Label(serial_settings_frame, text="COM-порт:").grid(row=1, column=1, sticky=tk.NW)

        self._comports_listbox = tk.Listbox(serial_settings_frame, width=20, height=2, selectmode='SINGLE')
        self.refresh_comports()

        tk.Label(serial_settings_frame, text="Скорость обмена\n данных по порту:").grid(row=2, column=1, sticky=tk.NW)

        self._baudrate_combobox = ttk.Combobox(serial_settings_frame, width=15)
        self._baudrate_combobox['values'] = (4800, 9600, 19200, 38400)
        self._baudrate_combobox.current(1)
        self._baudrate_combobox.grid(row=2, column=2, sticky=tk.NW)

        tk.Button(serial_settings_frame,
                  text="Подтвердить",
                  bg="yellow",
                  command=self.choose_comport_and_baudrate).grid(row=3, column=1, sticky=tk.NW)

        tk.Button(serial_settings_frame,
                  text="Обновить",
                  command=self.refresh_comports).grid(row=3, column=2, sticky=tk.NW)

    def choose_comport_and_baudrate(self):
        comports_chosen_indexes = self._comports_listbox.curselection()
        if len(comports_chosen_indexes) > 0:
            self._port = self._comports_listbox.get(comports_chosen_indexes[0])

        self._baudrate = self._baudrate_combobox.get()
        print("Информация по настройке:\nПорт:", self._port, "Baudrate:", self._baudrate)

    def refresh_comports(self):
        len_of_comports_listbox = self._comports_listbox.size()
        self._comports_listbox.delete(0, len_of_comports_listbox - 1)
        for comport in get_comports():
            self._comports_listbox.insert(tk.END, comport)
        self._comports_listbox.grid(row=1, column=2, sticky=tk.N)

    @property
    def port_and_baudrate(self):
        return self._port, self._baudrate

    @property
    def port(self):
        if self._port is None:
            raise ComportException("Порт не установлен")
        return self._port
    
    @property
    def baudrate(self):
        if self._baudrate is None:
            raise ComportException("Бодрэйт не установлен")
        return self._baudrate

