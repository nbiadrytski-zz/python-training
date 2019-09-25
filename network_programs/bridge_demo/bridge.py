import serial

sr = serial.Serial('/dev/tty.usbserial-14200', 115200)
sr.write(b'hello\n')

sr.s




print(sr.readline().decode('utf-8'))