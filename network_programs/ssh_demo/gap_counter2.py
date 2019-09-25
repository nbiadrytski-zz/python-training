import subprocess
import yaml
import RPi.GPIO as GPIO


SENSOR_PIN = 5
TARGET_POSITION = 6500
STARTING_SPEED = '0'
MAX_SPEED = '8480000'
MAX_ACCEL = '848000'
MAX_DECEL = '848000'
STEP_MODE = '8'  # 1/8 mode
CURRENT_LIMIT = '672'
DECAY_MODE = 'slow'
INITIAL_POSITION = '0'


def init_tic():
    """Initialise Tic with given params."""
    run_ticcmd('--starting-speed', STARTING_SPEED)
    run_ticcmd('--max-speed', MAX_SPEED)
    run_ticcmd('--max-accel', MAX_ACCEL)
    run_ticcmd('--max-decel', MAX_DECEL)
    run_ticcmd('--step-mode', STEP_MODE)
    run_ticcmd('--current', CURRENT_LIMIT)
    run_ticcmd('--decay', DECAY_MODE)
    run_ticcmd('--halt-and-set-position', INITIAL_POSITION)
    print('Reset current position to: {}.'.format(get_tic_status()['Current position']))
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


def sensor_state_changed():
    """True if optical sensor state was changed."""
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(SENSOR_PIN, GPIO.IN)
    return GPIO.event_detected(SENSOR_PIN)


def start_tic(target_position):
    """Run Tic with target_position argument"""
    run_ticcmd('--energize')
    run_ticcmd('--exit-safe-start', '--position', str(target_position))
    print('Tic is running!')


if __name__ == '__main__':
    init_tic()
    start_tic(TARGET_POSITION)

    gaps_list = []
    while get_tic_status()['Current position'] != TARGET_POSITION:
        if not sensor_state_changed():
            current_position = get_tic_status()['Current position']
            gaps_list.append(current_position)

    gaps = zip(gaps_list[::2], gaps_list[1::2])  # neighboring elems are tuples now
    for idx, gap in enumerate(list(gaps)):
        print('{}. Gap Start: {}. Gap End: {}. Gap: {}'.format(idx + 1, gap[0], gap[1], gap[1] - gap[0]))

    deenergize_tic()