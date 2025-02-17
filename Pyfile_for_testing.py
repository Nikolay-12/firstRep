import serial
import sys
import time

arduino = serial.Serial('COM4', 9600, timeout=10)
string = "$1 5; $0 3; $1 3; $0 5;"
#string_bytes = string.encode()
try:
    arduino.write(string.encode())
    print(string)
    #response = arduino.readline().decode()
    #print(response)
except OsError:
    print("Write failed!")
arduino.close()

'''
# Открываем Serial порт ('COMX' замените на имя вашего порта)
ser = serial.Serial('COM4', 9600)
# Отправляем строку "Hello, Arduino!" на Arduino, предварительно преобразовав ее в байты
ser.flush()
ser.write(string_bytes)
# Читаем ответ от Arduino через Serial порт
response = ser.readline()
# Декодируем ответ из байтов в строку с использованием UTF-8
decoded_response = response.decode('utf-8')
# Закрываем порт
ser.close()
print(decoded_response)

'''



'''        

# Configure the COM port
port = "COM4"  # Replace with the appropriate COM port name
baudrate = 9600

string = "Hello, Arduino!"
string_bytes = string.encode()

try:
    ser = serial.Serial(port, baudrate=baudrate)
    print("Serial connection established.")

    ser.write(string_bytes)
    # line = ser.readline().decode()
finally:
    ser.close()
    print("Serial connection closed.")
'''
'''    
# Получаем список доступных Serial портов
ports = list(serial.tools.list_ports.comports())
# Выводим информацию о каждом порте
for port in ports:
 print(f"Порт: {port.device}")
 print(f"Описание: {port.description}")
 print(f"Производитель: {port.manufacturer}\n")
 
# Открываем Serial порт ('COMX' замените на имя вашего порта)
ser = serial.Serial('COM4', 9600)

# Отправляем строку "Hello, Arduino!" на Arduino, предварительно преобразовав ее в байты
ser.write(b'Hello, Arduino!')
# Читаем ответ от Arduino через Serial порт
#response = ser.readline()
# Декодируем ответ из байтов в строку с использованием UTF-8
#decoded_response = response.decode('utf-8')
#decoded_response2 = response.decode('cp1252')
#print(response)
#print(decoded_response)
#print(decoded_response2)
# Закрываем порт
ser.close()
'''