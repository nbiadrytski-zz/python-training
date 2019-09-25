import subprocess
import yaml
import wiringpi
import csv

from libs.config_provider import ConfigProvider

config = ConfigProvider('config/gap_counter_settings.txt')
sensor_pin = int(config.get('opto_sensor_pin'))
target_position = int(config.get('target_position'))
gaps_list = []
pin_state = None


def init_tic():
    """Initialise Tic with given params."""
    run_ticcmd('--starting-speed', config.get('starting_speed'))
    run_ticcmd('--max-speed', config.get('max_speed'))
    run_ticcmd('--max-accel', config.get('max_accel'))
    run_ticcmd('--max-decel', config.get('max_decel'))
    run_ticcmd('--step-mode', config.get('step_mode'))
    run_ticcmd('--current', config.get('current_limit'))
    run_ticcmd('--decay', config.get('decay_mode'))
    # reset position to initial position, most likely to be 0
    run_ticcmd('--halt-and-set-position', config.get('initial_position'))
    print('Tic was initialised!')


def run_ticcmd(*args):
    """Run ticcmd command with given arguments."""
    return subprocess.check_output(['ticcmd'] + list(args))


def get_tic_status():
    """Get full status of Tic properties."""
    return yaml.safe_load(run_ticcmd('-s', '--full'))


def deenergize_tic():
    """Deenergize Tic."""
    run_ticcmd('--deenergize')
    print('Tic was deenergized!')


def start_tic(target_pos):
    """Energize and run Tic with target_position argument"""
    run_ticcmd('--energize')
    run_ticcmd('--exit-safe-start', '--position', str(target_pos))
    print('Tic is running!')


if __name__ == '__main__':
    # setup GPIO opto sensor pin to input mode
    # wiringpi.wiringPiSetupGpio()
    # wiringpi.pinMode(sensor_pin, wiringpi.GPIO.INPUT)

    def opto_call():
        global pin_state
        global gaps_list
        print('call')
        new_state = wiringpi.digitalRead(sensor_pin)
        if new_state != pin_state:
            pin_state = new_state
            gaps_list.append(get_tic_status()['Current position'])


    wiringpi.wiringPiSetupGpio()
    wiringpi.pinMode(sensor_pin, wiringpi.GPIO.INPUT)
    wiringpi.wiringPiISR(sensor_pin, wiringpi.GPIO.INT_EDGE_BOTH,
                         opto_call)

    # initialise and run tic
    init_tic()
    start_tic(target_position)
    print('started')

    # read initial sensor state, most likely will be 0
    # state will be changed to 1 when sensor detects the slot
    # and changed back to 0 when slot passes the sensor
    pin_state = wiringpi.digitalRead(sensor_pin)

    # gaps_list = []
    while get_tic_status()['Current position'] != target_position:
        pass
        # new_state = wiringpi.digitalRead(sensor_pin)
        # if new_state != pin_state:
        #    pin_state = new_state
        #    gaps_list.append(get_tic_status()['Current position'])

    gaps = zip(gaps_list[::2], gaps_list[1::2])
    for idx, gap in enumerate(list(gaps)):
        print('{}. Gap Start: {}. Gap End: {}. Gap: {}'.
              format(idx + 1, gap[0], gap[1], gap[1] - gap[0]))

    # write to csv
    # with open('results.csv', 'a') as f:
    #    writer = csv.writer(f, dialect='excel')
    #    writer.writerow(['Slot', 'Gap Start', 'Gap End', 'Gap'])
    #    for idx, gap in enumerate(list(gaps)):
    #        gaps = [idx + 1, gap[0], gap[1] - gap[0]]
    #        writer.writerow(gaps)

    deenergize_tic()