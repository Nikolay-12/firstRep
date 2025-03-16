from tkinter import DoubleVar
import tkinter as tk
from tkinter.messagebox import showerror

DEFAULT_KP = 3
DEFAULT_KI = 2
DEFAULT_KD = 1


class PidSettings:
    def __init__(self, parent, floating_point_validation_function) -> None:
        self._kp = DoubleVar(value=DEFAULT_KP)
        self._ki = DoubleVar(value=DEFAULT_KI)
        self._kd = DoubleVar(value=DEFAULT_KD)
        self.parent = parent
        self.floating_point_validation_function = floating_point_validation_function

    def ui_draw(self):
        pid_settings_frame = tk.LabelFrame(self.parent, padx=15, pady=10, text="Коэффициенты ПИД")
        pid_settings_frame.grid(padx=10, pady=5, row=2, column=1, sticky=tk.NSEW)
        tk.Label(pid_settings_frame, text="Kp:").grid(row=1, column=1)
        tk.Label(pid_settings_frame, text="Ki:").grid(row=1, column=3)
        tk.Label(pid_settings_frame, text="Kd:").grid(row=1, column=5)

        entry_Kp = tk.Entry(
            pid_settings_frame,
            validate="key",
            validatecommand=self.floating_point_validation_function,
            textvariable=self._kp,
            width=5,
        )
        entry_Kp.grid(row=1, column=2, sticky=tk.W)
        entry_Ki = tk.Entry(
            pid_settings_frame,
            validate="key",
            validatecommand=self.floating_point_validation_function,
            textvariable=self._ki,
            width=5,
        )
        entry_Ki.grid(row=1, column=4, sticky=tk.W)
        entry_Kd = tk.Entry(
            pid_settings_frame,
            validate="key",
            validatecommand=self.floating_point_validation_function,
            textvariable=self._kd,
            width=5,
        )
        entry_Kd.grid(row=1, column=6, sticky=tk.W)
        tk.Button(
            pid_settings_frame,
            text="Изменить",
            bg="yellow",
            command=self.print_pid_parameters).grid(row=3, column=6)

    def print_pid_parameters(self):
        try:
            print("Коэффициенты ПИД регулятора:", self.kp, self.ki, self.kd)
        except (tk.TclError):
            showerror(title='Ошибка', message='Некоторые коэффициенты ПИД-регулятора не заданы, перепроверьте их!')

    @property
    def pid_parameters(self):
        return self._kp.get(), self._ki.get(), self._kd.get()

    @property
    def kp(self):
        return self._kp.get()

    @property
    def ki(self):
        return self._ki.get()

    @property
    def kd(self):
        return self._kd.get()
