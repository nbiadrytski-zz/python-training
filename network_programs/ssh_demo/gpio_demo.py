import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BOARD)
GPIO.setup(5, GPIO.IN)
while True:
    if GPIO.event_detected(5):
        print('Sensor state changed: getting current position...')


# To read the state
# state = GPIO.input(26)
# if state:
#    print('on')
# else:
#    print('off')

