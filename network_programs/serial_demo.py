import serial

sr = serial.Serial('/dev/tty.usbserial-14200', 115200)
sr.write(b'hello\n')





print(sr.readline().decode('utf-8'))
