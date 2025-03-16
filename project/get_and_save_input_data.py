import tkinter as tk
from functools import partial
from tkinter import filedialog
from tkinter.messagebox import showerror, showinfo

from comport_settings import ComportSettings
from pid_settings import PidSettings
from scenario_control_settings import ScenarioControlSetttings
from manual_control_settings import ManualControlSettings
from list_of_connected_devices import ListOfConnectedDevices
from utils.floating_point_validation import is_valid_floating_point

class GetAndSaveInputData:
    def __init__(self, parent):
        self.parent = parent

    def ui_draw(self):
        additional_features_frame = tk.LabelFrame(self.parent, padx=15, pady=10, text="Дополнительные возможности")
        additional_features_frame.grid(padx=10, pady=5, row=5, column=1, sticky=tk.NSEW)
        tk.Label(additional_features_frame, text="Введенные данные:").grid(row=1, column=1)
        tk.Button(
            additional_features_frame,
            text="Получить",
            #command=partial(self.get_input_data, port_and_baudrate, pid_parameters, scenario_file_address,
                            #all_manual_settings, connected_devices)).grid(row=1, column=2)
            command=self.get_input_data).grid(row=1, column=2)
        tk.Label(additional_features_frame, text="Сохранение данных:").grid(row=2, column=1)
        tk.Button(
            additional_features_frame,
            text="Сохранить",
            command=self.save_input_data).grid(row=2, column=2)

    #def update(self, port_and_baudrate, pid_parameters, scenario_file_address, all_manual_settings, connected_devices):
        #print(pid_parameters)

    def get_input_data(self):
        self.port_and_baudrate = self.parent.comport_settings.port_and_baudrate
        self.pid_parameters = self.parent.pid_setting.pid_parameters
        self.scenario_file_address = self.parent.scenario_control_setting.scenario_file_address
        self.all_manual_settings = self.parent.manual_control_setting.all_manual_settings
        self.connected_devices = self.parent.list_of_used_devices.connected_devices
        print(f'Выбранный порт: {self.port_and_baudrate[0]}; Baud rate: {self.port_and_baudrate[1]}\n'
              f'Коэффициенты ПИД: {self.pid_parameters} ;\n'
              f'Режим работы (сценарий-0/ручной-1): ;\n'
              f'Адрес файла-сценария: {self.scenario_file_address} ;\n'
              f'Настройки ручного режима управления: {self.all_manual_settings} ;\n'
              f'Подключенные устройства: {self.connected_devices}\n')
    '''
    def get_input_data(self, port_and_baudrate, pid_parameters, scenario_file_address, all_manual_settings, connected_devices):
        self.update_variables(self, port_and_baudrate, pid_parameters, scenario_file_address, all_manual_settings, connected_devices)
        print(self.pid_parameters)
    '''

    def save_input_data(self):
        self.port_and_baudrate = self.parent.comport_settings.port_and_baudrate
        self.pid_parameters = self.parent.pid_setting.pid_parameters
        self.scenario_file_address = self.parent.scenario_control_setting.scenario_file_address
        self.all_manual_settings = self.parent.manual_control_setting.all_manual_settings
        self.connected_devices = self.parent.list_of_used_devices.connected_devices
        if (self.port_and_baudrate[0] == None):
            showinfo(title="Внимание", message="Порт не выбран! Запустить измерение не получится.")
        if (len(self.connected_devices) == 0):
            showinfo(title="Внимание", message="Не выбраны подключенные устройства! Запустить измерение не получится.")
        saved_file_path = filedialog.asksaveasfilename(initialfile="Untitled.txt", filetypes=[("Text files", "*.txt")])
        try:
            f = open(saved_file_path, 'w+')
            f.writelines( f'Выбранный порт: {self.port_and_baudrate[0]}; Baud rate: {self.port_and_baudrate[1]}\n'
                          f'Коэффициенты ПИД: {self.pid_parameters} ;\n'
                          f'Режим работы (сценарий-0/ручной-1): ;\n'
                          f'Адрес файла-сценария: {self.scenario_file_address} ;\n'
                          f'Настройки ручного режима управления: {self.all_manual_settings} ;\n'
                          f'Подключенные устройства: {self.connected_devices}\n')
            f.close()
        except FileNotFoundError:
            showerror(title="Ошибка", message="Не выбрана директория")

    @classmethod
    def update_variables(cls, port_and_baudrate, pid_parameters, scenario_file_address, all_manual_settings, connected_devices):
        cls.port_and_baudrate = port_and_baudrate
        cls.pid_parameters = pid_parameters
        cls.scenario_file_address = scenario_file_address
        cls.all_manual_settings = all_manual_settings
        cls.connected_devices = connected_devices
        #return cls.port_and_baudrate, cls.pid_parameters, cls.scenario_file_address, cls.all_manual_settings, cls.connected_devices
