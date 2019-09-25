import subprocess
import yaml
import threading
import wiringpi
import RPi.GPIO as GPIO


def run_ticcmd(*args):
    return subprocess.check_output(['ticcmd'] + list(args))


def get_tic_status():
    return yaml.safe_load(run_ticcmd('-s', '--full'))


# def get_current_position():
#     t = threading.Timer(3.0, get_current_position)
#     t.start()
#     status = get_tic_status()
#     print('Current position: {}.'.format(status['Current position']))
#     if status['Current position'] == 6500:
#         t.cancel()

def get_current_position():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(5, GPIO.IN)
    while True:
        if GPIO.event_detected(5):
            print('Sensor state changed: getting current position...')
            status = get_tic_status()
            print('Current position: {}.'.format(status['Current position']))


def start_tic(target_position):
    run_ticcmd('--exit-safe-start', '--position', str(target_position))


# def read_sensor():
#     # initialise GPIO mode
#     wiringpi.wiringPiSetupGpio()
#     # set the mode of a pin to either INPUT, OUTPUT, PWM_OUTPUT or GPIO_CLOCK
#     wiringpi.pinMode(pin=5, mode=wiringpi.GPIO.INPUT)
#     result = wiringpi.digitalRead(5)  # read from pin 5
#     return result


# def setup_opto_sensor(callback):
#     def opto_call():
#         if 1 == wiringpi.digitalRead(5):
#             callback()
#     wiringpi.wiringPiSetupGpio()
#     wiringpi.pinMode(5, wiringpi.GPIO.INPUT)
#     wiringpi.wiringPiISR(5, wiringpi.GPIO.INT_EDGE_RISING,
#                          opto_call)



if __name__ == '__main__':
    start_tic(6500)
    get_current_position()

