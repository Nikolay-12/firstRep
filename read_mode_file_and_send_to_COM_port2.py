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
print(command_line) # команда целиком из выбранного файла
print(line_counter) # сколько элементарных команд придется выполнить (количество строк в файле)

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

def selected_COM(): # Функция для отправки данных на ардуинку и которая может получать подтверждение от неё
    select = list(List1.curselection())
    port = connected[int(select[0])]
    baudrate = 9600
    line_counter_for_func = line_counter
    try:
        ser = serial.Serial(port, baudrate=baudrate)
        print("Serial connection established.")

        while line_counter_for_func + 1 > 0:
            ser.write(command_line.encode())
            line = ser.readline().decode().strip()

            if line:
                print("Received:", line)
                print("line_counter:", line_counter_for_func)
                line_counter_for_func -= 1

    except serial.SerialException as se:
        print("Serial port error:", str(se))

    except KeyboardInterrupt:
        pass

    finally:
        if ser.is_open:
            ser.close()
            print("Serial connection closed.")


B1 = tkinter.Button(window, text = 'Загрузить данные', width = 50, height = 5, command = selected_COM)
B1.pack()

window.mainloop()


'''
def test():
    line_counter_for_func = line_counter
    try:
        print('Связь есть')
        print(command_line)
        print(line_counter_for_func)
        while line_counter_for_func + 1 > 0:
            print('Пробуем')
            line_counter_for_func -= 1
    finally:
        print('Закругляемся!')
'''
'''
array1 = []
for line in f:
    print(line.strip())
    numbers = re.findall(r'\d+', line) # использование регулярных выражений для нахождения чисел в строке
    numbers = [int(i) for i in numbers]
    if len(numbers)!=2:
        print("Проверь файл, режим работы задан неправильно (в строке должно быть 2 числа: температура и время отжига на ней)")
        break
    else:
        print("температура = ", numbers[0], "°C; время отжига = ", numbers[1], " мин")

    array1 += numbers # добавляем элементы в массив, который мы и будем отправлять на ардуино
f.close()
print(array1)
'''
