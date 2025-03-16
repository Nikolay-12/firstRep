from tkinter import DoubleVar
import tkinter as tk
from tkinter.messagebox import showerror

class ManualControlSettings:
    def __init__(self, parent, floating_point_validation_function) -> None:
        self._Tmax = DoubleVar(value=0)
        self._delta_T = DoubleVar(value=0)
        self._delta_t = DoubleVar(value=0)
        self._number_of_values_for_averaging = DoubleVar(value=0)
        self._data_reading_frequency = DoubleVar(value=0)
        self.parent = parent
        self.floating_point_validation_function = floating_point_validation_function

    def ui_draw(self):
        manual_control_settings_frame = tk.LabelFrame(self.parent, padx=15, pady=10, text="Ручное управление")
        manual_control_settings_frame.grid(padx=10, pady=5, row=4, column=1, sticky=tk.NSEW)
        tk.Label(manual_control_settings_frame, text="T_max").grid(row=1, column=1)
        tk.Label(manual_control_settings_frame, text="ΔT").grid(row=1, column=3)
        tk.Label(manual_control_settings_frame, text="Δt").grid(row=1, column=5)

        entry_T_max = tk.Entry(
            manual_control_settings_frame,
            validate="key",
            validatecommand=self.floating_point_validation_function,
            textvariable=self._Tmax,
            width=5
        )
        entry_T_max.grid(row=1, column=2, sticky=tk.W)
        entry_delta_T = tk.Entry(
            manual_control_settings_frame,
            validate="key",
            validatecommand=self.floating_point_validation_function,
            textvariable=self._delta_T,
            width=5
        )
        entry_delta_T.grid(row=1, column=4, sticky=tk.W)
        entry_delta_t = tk.Entry(
            manual_control_settings_frame,
            validate="key",
            validatecommand=self.floating_point_validation_function,
            textvariable=self._delta_t,
            width=5
        )
        entry_delta_t.grid(row=1, column=6, sticky=tk.W)

        tk.Label(manual_control_settings_frame, text="<...>n").grid(row=2, column=1)
        tk.Label(manual_control_settings_frame, text="Δt_R&T").grid(row=2, column=3)
        # <...>n -- к-во съемок\n для усреднения
        # Δt_R&T -- периодичность\n съемки R и T

        entry_number_of_values_for_averaging = tk.Entry(
            manual_control_settings_frame,
            validate="key",
            validatecommand=self.floating_point_validation_function,
            textvariable=self._number_of_values_for_averaging,
            width=5
        )
        entry_number_of_values_for_averaging.grid(row=2, column=2, sticky=tk.W)
        entry_data_reading_frequency = tk.Entry(
            manual_control_settings_frame,
            validate="key",
            validatecommand=self.floating_point_validation_function,
            textvariable=self._data_reading_frequency,
            width=5
        )
        entry_data_reading_frequency.grid(row=2, column=4, sticky=tk.W)
        tk.Button(
            manual_control_settings_frame,
            text="Запустить",
            bg="Green",
            command=self.start_measurement_in_manual_mode).grid(row=3, column=1, columnspan=2)
        tk.Button(
            manual_control_settings_frame,
            text="Приостановить",
            bg="Red",
            command=self.stop_measurement_in_manual_mode).grid(row=3, column=4, columnspan=3)

    def start_measurement_in_manual_mode(self):
        try:
            print("Настройки ручного режима управления: T_max =", self.Tmax, "; ΔT =", self.delta_T, "; Δt =", self.delta_t,
              "; <...>n =", self.number_of_values_for_averaging, "; Δt_R&T =", self.data_reading_frequency)
        except (tk.TclError):
            showerror(title='Ошибка', message='Некоторые настройки ручного режима управления не заданы, перепроверьте их!')


    def stop_measurement_in_manual_mode(self):
            print("Функция пока не готова")

    @property
    def all_manual_settings(self):
        return self._Tmax.get(), self._delta_T.get(), self._delta_t.get(), \
               self._number_of_values_for_averaging.get(), self._data_reading_frequency.get()

    @property
    def Tmax(self):
        return self._Tmax.get()

    @property
    def delta_T(self):
        return self._delta_T.get()

    @property
    def delta_t(self):
        return self._delta_t.get()

    @property
    def number_of_values_for_averaging(self):
        return self._number_of_values_for_averaging.get()

    @property
    def data_reading_frequency(self):
        return self._data_reading_frequency.get()