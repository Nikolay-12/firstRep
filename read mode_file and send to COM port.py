import os
from pathlib import Path
import  tkinter as tk
from tkinter import filedialog
from array import *
import re
import serial.tools.list_ports

# выбор пользователем файла для чтения
root = tk.Tk()
root.withdraw()
file_path = filedialog.askopenfilename()
print(file_path)

# file_path = Path('C:/Users/malin/OneDrive/Рабочий стол/Коля/ВУЗ/лаба/проект с печкой/mode_file.txt')

f = open(file_path, 'r', encoding='cp1252') # открывается выбранный файл и читается построчно
array = []
for line in f:
    print(line.strip())
    numbers = re.findall(r'\d+', line) # использование регулярных выражений для нахождения чисел в строке
    numbers = [int(i) for i in numbers]
    if len(numbers)!=2:
        print("Проверь файл, режим работы задан неправильно (в строке должно быть 2 числа: температура и время отжига на ней)")
        break
    else:
        print("температура = ", numbers[0], "°C; время отжига = ", numbers[1], " мин")

    array += numbers # добавляем элементы в массив, который мы и будем отправлять на ардуино
f.close()
print(array)
command = str(array[0]) + " " + str(array[1])
del array[0:2]
print(array)
print(command)
'''
# Определяем на какой порт мы будем отправлять данные
list1 = serial.tools.list_ports.comports()
connected = []

for element in list1:
    connected.append(element.device)
print("connected COM ports: " + str(connected)) # какие порты доступны

window = tkinter.Tk()
window.title("Сбор данных")
window.geometry("600x600")

L1 = tkinter.Label(window, text = 'программа по загрузке данных на подключенные устройства', width = 100, height = 10, font = 'Arial 14')
L1.pack()

List1 = tkinter.Listbox(window, width = 50, height = 5, selectmode = 'SINGLE')
for i in range(len(connected)):
    List1.insert(tkinter.END, connected[i]) # показываем пользователю какие порты ему доступны и он выбирает нужный
List1.pack()

def selected_COM():
    try:
        select = list(List1.curselection())
        print(select)
        r = serial.Serial(connected[int(select[0])], 9600, timeout = 1)
        print("Соединение с портом установлено")
        while len(array)>0:
            command = str(array[0]) + " " + str(array[1])
            del array[0:2]
            ser.write(command.encode())
    
    except serial.SerialException as se:
        print("Ошибка сериал порта:", str(se))

    except KeyboardInterrupt:
        pass

    finally:
        # В конце работы прерываем соединение
        if ser.is_open:
            ser.close()
            print("Соединение прервано")

B1 = tkinter.Button(window, text = 'Загрузить данные', width = 50, height = 5, command = selected_COM)
B1.pack()

window.mainloop()


# Configure the COM port
port = "COM3"  # Replace with the appropriate COM port name
baudrate = 9600

try:
    # Open the COM port
    ser = serial.Serial(port, baudrate=baudrate)
    print("Serial connection established.")

    # Send commands to the Arduino
    while True:
        command = input("Enter a command (e.g., 'ON', 'OFF'): ")

        # Send the command to the Arduino
        ser.write(command.encode())
'''
