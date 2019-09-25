import serial

#ser = serial.serial_for_url("socket://127.0.0.1:65432/logging=debug")
ser = serial.serial_for_url('/dev/tty.usbserial-14200', do_not_open=False)
# args.SERIALPORT, do_not_open=True
#ser = serial.Serial('/dev/tty.usbserial-14200', 115200)
data = ser.write(b'hello')
if data:
    print(data)
    ser.flushOutput()
ser.close()