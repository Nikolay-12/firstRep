import tkinter as tk
from tkinter.ttk import Checkbutton
from tkinter import BooleanVar

from information_from_connected_devices import InformationFromConnectedDevices

Number_of_thermocouples = 9
Number_of_sensors = 16

class ListOfConnectedDevices:
    def __init__(self, parent) -> None:
        self._connected_devices = []
        self.parent = parent
        self._checking_selected_sensors = dict()
        self._checking_selected_thermocouples = dict()
        for i in range(1, Number_of_sensors + 1):
            self._checking_selected_sensors[i] = BooleanVar(value=False)
        for i in range(1, Number_of_thermocouples + 1):
            self._checking_selected_thermocouples[i] = BooleanVar(value=False)

    def ui_draw(self):
        connected_devices_frame = tk.LabelFrame(self.parent, padx=15, pady=10, text="Подключенные сенсоры и термопары")
        connected_devices_frame.grid(padx=10, pady=5, row=1, column=2, sticky=tk.NSEW)
        for i in range(1, Number_of_sensors + 1):
            tk.Label(connected_devices_frame, text="R%i" % i).grid(row=1, column=i)
            Checkbutton(
                connected_devices_frame,
                variable=self._checking_selected_sensors[i]).grid(row=2, column=i)

        for i in range(1, Number_of_thermocouples + 1):
            tk.Label(connected_devices_frame, text="T%i" % i).grid(row=3, column=i)
            Checkbutton(
                connected_devices_frame,
                var=self._checking_selected_thermocouples[i]).grid(row=4, column=i)
        tk.Button(
            connected_devices_frame,
            text="Подтвердить",
            bg="yellow",
            command=self.confirm_selected_devices).grid(row=3, column=13, rowspan=2, columnspan=4)

    def confirm_selected_devices(self):
        self._connected_devices = []
        for i in range(1, Number_of_sensors + 1):
            if (self._checking_selected_sensors[i].get() == 1):
                self._connected_devices.append("R%i"%i)
        for i in range(1, Number_of_thermocouples + 1):
            if (self._checking_selected_thermocouples[i].get() == 1):
                self._connected_devices.append("T%i"%i)
        print("Подключенные устройства:", self.connected_devices)
        self.parent.info_from_used_devices.update_color(self.connected_devices)

    @property
    def connected_devices(self):
        return self._connected_devices