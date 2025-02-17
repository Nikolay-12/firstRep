# import os
# import  tkinter
import  tkinter as tk
from tkinter import filedialog
# import serial
import serial.tools.list_ports

# выбор пользователем файла для чтения
root = tk.Tk()
root.withdraw()
file_path = filedialog.askopenfilename()
print(file_path)

# from pathlib import Path
# file_path = Path('C:/Users/malin/OneDrive/Рабочий стол/Коля/ВУЗ/лаба/проект с печкой/mode_file.txt')

f = open(file_path, 'r', encoding='cp1252') # открывается выбранный файл и читается построчно
command_line = ''
line_counter = 0
for line in f:
    #print(line.strip())
    command_line += line.strip() + ' '
    line_counter += 1
f.close()
print(command_line)
print(line_counter)

