import threading
import time


class MyThread(threading.Thread):
    def __init__(self, thread_id, name, counter):
        threading.Thread.__init__(self)
        self.thread_id = thread_id
        self.name = name
        self.counter = counter

    def run(self):
        print(f'Starting {self.name}')
        print_time(self.name, 5, self.counter)
        print(f'Exiting {self.name}')


def print_time(thread_name, delay, counter):
    while counter:
        time.sleep(delay)
        print(f'{thread_name}: {time.ctime(time.time())}')
        counter -= 1