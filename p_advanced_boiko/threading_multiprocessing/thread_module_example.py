import _thread
import time


def print_time(thread_name, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print(f'{thread_name}: {time.ctime(time.time())}')


if __name__ == '__main__':
    try:
        _thread.start_new_thread(print_time, ('Thread-1', 2))
        _thread.start_new_thread(print_time, ('Thread-2', 4))
    except Exception as e:
        print(f'Error: unable to start thread. {e}')

    while True:
        pass

# Thread-1: Fri Mar 22 15:15:07 2019
# Thread-2: Fri Mar 22 15:15:09 2019
# Thread-1: Fri Mar 22 15:15:09 2019
# Thread-1: Fri Mar 22 15:15:11 2019
# Thread-2: Fri Mar 22 15:15:13 2019
# Thread-1: Fri Mar 22 15:15:13 2019
# Thread-1: Fri Mar 22 15:15:15 2019
# Thread-2: Fri Mar 22 15:15:17 2019
# Thread-2: Fri Mar 22 15:15:21 2019
# Thread-2: Fri Mar 22 15:15:25 2019


