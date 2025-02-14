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
for line in f:
    print(line.strip())
    numbers = re.findall(r'\d+', line) # использование регулярных выражений для нахождения чисел в строке
    numbers = [int(i) for i in numbers]
    print(numbers)
    if len(numbers)!=2:
        print("Проверь файл, режим работы задан неправильно (в строке должно быть 2 числа: температура и время отжига на ней)")
        break
    else:
        print("температура = ", numbers[0], "°C; время отжига = ", numbers[1], " мин")
f.close()

# print(lines)

'''
Для выделения вещественных чисел
nums = re.findall(r'\d*\.\d+|\d+', s)
nums = [float(i) for i in nums]


numbers = ''.join(c if c.isdigit() else ' ' for c in line).split() 
print(numbers)
while True:
    line = f.readline()  # считываем строку
    if not line:  # прерываем цикл, если строка пустая
        break
    numbers = ''.join(c if c.isdigit() else ' ' for c in line).split()

    print(line.strip()) # выводим строку
    print(numbers)  # выводим цифры из строки
lines = f.read().split('\n')
numbers = ''.join(c if c.isdigit() else ' ' for c in line).split()
print(numbers)
'''