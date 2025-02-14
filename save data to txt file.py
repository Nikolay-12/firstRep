import serial
import re
import time
import tkinter
import serial.tools.list_ports
from datetime import datetime
#from tkinter import *
#from tkinter import ttk

list1 = serial.tools.list_ports.comports()
connected = []

for element in list1:
    connected.append(element.device)
print("connected COM ports: " + str(connected))

window = tkinter.Tk()
window.title("Сбор данных")
window.geometry("600x600")

L1 = tkinter.Label(window, text = 'программа по считыванию данных с подключенных устройств', width = 100, height = 10, font = 'Arial 14')
L1.pack()

List1 = tkinter.Listbox(window, width = 50, height = 5, selectmode = 'SINGLE')
for i in range(len(connected)):
    List1.insert(tkinter.END, connected[i])
List1.pack()

def selected_COM():
    select = list(List1.curselection())
    print(select)
    r = serial.Serial(connected[int(select[0])], 9600, timeout = 1)
    f = open('test.txt', 'w')
    glossary = '0123456789,. ' # словарик, который передаёт нам из COM-порта только цифры и знаки препинания
    for i in range(20): # собираем 20 показаний
        s = ''
        N = str(r.readline()) # чтение данных из выбранного СОМ-порта и перевод в строку
        N1 = ''.join([ch for ch in N if ch in glossary])
        '''
        result = re.findall(r'\d', N) # функция findall библиотеки регулярных выражений re отбрасывает буквенные значения
        for i in range (len(result)):
            s += result[i]
        '''
        f.write(datetime.now().strftime("%Y-%m-%d_%H:%M:%S  ") + N1 + '\n')
    f.close()

B1 = tkinter.Button(window, text = 'Получить данные', width = 50, height = 5, command = selected_COM)
B1.pack()

window.mainloop()