# import os
# from pathlib import Path
import  tkinter
import  tkinter as tk
from tkinter import filedialog
# from array import *
# import re
import serial
import serial.tools.list_ports

# выбор пользователем файла для чтения
root = tk.Tk()
root.withdraw()
file_path = filedialog.askopenfilename()
print(file_path)

f = open(file_path, 'r', encoding='cp1252') # открывается выбранный файл и читается построчно
command_line = ''
line_counter = 0
for line in f:
    command_line += line.strip() + ' '
    line_counter += 1
f.close()
print(command_line)
print(line_counter)

port = "COM4"
baudrate = 9600

try:
    ser = serial.Serial(port, baudrate=baudrate)
    print("Serial connection established.")

    while line_counter + 1 > 0:
        ser.write(command_line.encode())
        line = ser.readline().decode().strip()

        if line:
            print("Received:", line)
            print("line_counter:", line_counter)
            line_counter -= 1

except serial.SerialException as se:
    print("Serial port error:", str(se))

except KeyboardInterrupt:
    pass

finally:
    if ser.is_open:
        ser.close()
        print("Serial connection closed.")


'''
# Определяем на какой порт мы будем отправлять данные
list1 = serial.tools.list_ports.comports()
connected = []

for element in list1:
    connected.append(element.device)
print("connected COM ports: " + str(connected))  # какие порты доступны

window = tkinter.Tk()
window.title("Сбор данных")
window.geometry("600x600")

L1 = tkinter.Label(window, text='программа по загрузке данных на подключенные устройства', width=100, height=10,
                   font='Arial 14')
L1.pack()

List1 = tkinter.Listbox(window, width=50, height=5, selectmode='SINGLE')
for i in range(len(connected)):
    List1.insert(tkinter.END, connected[i])  # показываем пользователю какие порты ему доступны и он выбирает нужный
List1.pack()


def selected_COM():
    select = list(List1.curselection())
    print(select)
    ser = serial.Serial(connected[int(select[0])], 9600, timeout=1)
    print("Соединение с портом установлено")
    print(command_line)
    ser.write(command_line.encode())

    response = ser.readline()
    # Декодируем ответ из байтов в строку с использованием cp1252
    decoded_response = response.decode('cp1252')
    # Закрываем порт
    ser.close()
    print(decoded_response)
    print("Соединение прервано")


# arr = array1('i', array)
B1 = tkinter.Button(window, text='Загрузить данные', width=50, height=5, command=selected_COM)
B1.pack()

window.mainloop()
'''

'''
select = list(List1.curselection())
    print(select)
    ser = serial.Serial(connected[int(select[0])], 9600, timeout=1)
    print("Соединение с портом установлено")
    print(command_line)
    ser.write(command_line.encode())

    response = ser.readline()
    # Декодируем ответ из байтов в строку с использованием cp1252
    decoded_response = response.decode('cp1252')
    # Закрываем порт
    ser.close()
    print(decoded_response)
    print("Соединение прервано")

    try:
        select = list(List1.curselection())
        print(select)
        ser = serial.Serial(connected[int(select[0])], 9600, timeout=1)
        print("Соединение с портом установлено")
        print(command_line)
        ser.write(command_line.encode())
        #ser.write(command_line)

        response = ser.readline()
        # Декодируем ответ из байтов в строку с использованием UTF-8
        decoded_response = response.decode('utf-8')
        # Закрываем порт
        ser.close()
        print(decoded_response)

    except serial.SerialException as se:
        print("Ошибка сериал порта:", str(se))

    except KeyboardInterrupt:
        pass

    finally:
        # В конце работы прерываем соединение
        if ser.is_open:
            ser.close()
            print("Соединение прервано")

'''