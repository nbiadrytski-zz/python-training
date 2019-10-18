import time


def check_time(param, timeout, poll_time):
    # ping_done = False
    # https://stackoverflow.com/questions/24374620/python-loop-to-run-for-certain-amount-of-seconds
    end_time = time.monotonic() + timeout
    while time.monotonic() <= end_time:
        if param == 'test':
            # ping_done = True
            return True
        else:
            print('try again!')
            time.sleep(poll_time)
    raise TimeoutError('No response from server!!!')


if __name__ == '__main__':
    print(check_time(param='tpest', timeout=20, poll_time=2))
