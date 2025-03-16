import tkinter as tk

from comport_settings import ComportSettings
from pid_settings import PidSettings
from scenario_control_settings import ScenarioControlSetttings
from manual_control_settings import ManualControlSettings
from list_of_connected_devices import ListOfConnectedDevices
from get_and_save_input_data import GetAndSaveInputData
from plotting import Plotting
from information_from_connected_devices import InformationFromConnectedDevices
from working_with_devices_via_COM_port import WorkingWithDevicesViaCOMPort
from utils.floating_point_validation import is_valid_floating_point


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        check_floating_point = (self.register(is_valid_floating_point), "%P")

        self.comport_settings = ComportSettings(self)
        self.comport_settings.ui_draw()

        self.pid_setting = PidSettings(self, check_floating_point)
        self.pid_setting.ui_draw()

        self.scenario_control_setting = ScenarioControlSetttings(self, check_floating_point)
        self.scenario_control_setting.ui_draw()

        self.manual_control_setting = ManualControlSettings(self, check_floating_point)
        self.manual_control_setting.ui_draw()

        self.list_of_used_devices = ListOfConnectedDevices(self)
        self.list_of_used_devices.ui_draw()

        #self.get_and_save_data = GetAndSaveInputData(self, self.comport_settings.port_and_baudrate,
        #    self.pid_setting.pid_parameters, self.scenario_control_setting.scenario_file_address,
        #    self.manual_control_setting.all_manual_settings, self.list_of_used_devices.connected_devices)
        '''
        self.get_and_save_data.update(self.comport_settings.port_and_baudrate,
        self.pid_setting.pid_parameters, self.scenario_control_setting.scenario_file_address,
        self.manual_control_setting.all_manual_settings, self.list_of_used_devices.connected_devices)
        '''
        self.get_and_save_data = GetAndSaveInputData(self)
        self.get_and_save_data.ui_draw()

        self.graph_plotting = Plotting(self, check_floating_point)
        self.graph_plotting.ui_draw()

        self.info_from_used_devices = InformationFromConnectedDevices(self)
        self.info_from_used_devices.ui_draw()

        self.working_with_devices_by_COM_port = WorkingWithDevicesViaCOMPort(self)
    '''
    def updateApp(self):
        self.get_and_save_data.update_variables(self.comport_settings.port_and_baudrate,
                            self.pid_setting.pid_parameters, self.scenario_control_setting.scenario_file_address,
                            self.manual_control_setting.all_manual_settings,
                            self.list_of_used_devices.connected_devices)

        self.get_and_save_data = GetAndSaveInputData(self, self.comport_settings.port_and_baudrate,
                            self.pid_setting.pid_parameters, self.scenario_control_setting.scenario_file_address,
                            self.manual_control_setting.all_manual_settings,
                            self.list_of_used_devices.connected_devices)
        self.get_and_save_data.ui_draw()
    '''

if __name__ == "__main__":
    app = App()
    app.title("Интерфейс пользователя печки")
    #app.updateApp()
    app.mainloop()

