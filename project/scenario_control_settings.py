import tkinter as tk
from tkinter import IntVar, StringVar
from tkinter.messagebox import showerror
from tkinter import filedialog
import re

from working_with_devices_via_COM_port import WorkingWithDevicesViaCOMPort

class ScenarioControlSetttings:
    def __init__(self, parent, floating_point_validation_function) -> None:
        self._scenario_file_address = StringVar(value='')
        self._command_line = StringVar(value='')
        self._line_counter = IntVar(value=0)
        self.parent = parent
        self.floating_point_validation_function = floating_point_validation_function

    def ui_draw(self):
        scenario_control_settings_frame = tk.LabelFrame(self.parent, padx=15, pady=10, text="Управление по сценарию")
        scenario_control_settings_frame.grid(padx=10, pady=5, row=3, column=1, sticky=tk.NSEW)
        tk.Label(scenario_control_settings_frame, text="Сценарий:").grid(row=1, column=1)
        tk.Button(
            scenario_control_settings_frame,
            text="Выбрать",
            command=self.choose_mode_file).grid(row=1, column=2,sticky=tk.W)

        tk.Label(scenario_control_settings_frame, text="Адрес файла:").grid(row=2, column=1)
        tk.Entry(
            scenario_control_settings_frame,
            state='disabled',
            textvariable=self._scenario_file_address).grid(row=2, column=2)  # , sticky=tk.NSEW
        tk.Button(
            scenario_control_settings_frame,
            text="Запустить\n сценарий",
            bg="Green",
            command=self.start_measurement_in_scenario_mode).grid(row=3, column=1)
        tk.Button(
            scenario_control_settings_frame,
            text="Приостановить\n сценарий",
            bg="Red",
            command=self.stop_measurement_in_scenario_mode).grid(row=3, column=2)

    def choose_mode_file(self):
        file_path = filedialog.askopenfilename()
        self._scenario_file_address.set(file_path)
        print("Был выбран файл:", file_path)

    def start_measurement_in_scenario_mode(self):
        try:
            file_path = self.scenario_file_address
            f = open(file_path, 'r', encoding='cp1252')
            self._command_line.set(value='')
            self._line_counter.set(value=0)
            for line in f:
                    new_line = line.replace('\n', '; ')
                    self._command_line.set(self.command_line + new_line)
                    self._line_counter.set(self.line_counter + 1)
            f.close()
            print("Данные из файла", self.scenario_file_address, ": ", self.command_line, "\nКоличество команд:", self.line_counter)
            self.parent.working_with_devices_by_COM_port.read_data_from_devices_and_write_it()
            #self.parent.working_with_devices_by_COM_port.start_working_on_the_script()
        except FileNotFoundError:
            showerror(title='Ошибка', message='Файл не выбран!')

    def stop_measurement_in_scenario_mode(self):
        print("Функция пока не готова")

    @property
    def all_scenario_settings(self):
        return self._scenario_file_address.get(), self._command_line.get(), self._line_counter.get()

    @property
    def scenario_file_address(self):
        return self._scenario_file_address.get()

    @property
    def command_line(self):
        return self._command_line.get()

    @property
    def line_counter(self):
        return self._line_counter.get()