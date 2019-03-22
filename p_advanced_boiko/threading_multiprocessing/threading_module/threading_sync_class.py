import threading
import time


class MyThread(threading.Thread):

    thread_lock = threading.Lock()

    def __init__(self, thread_id, name, counter):
        threading.Thread.__init__(self)
        self.thread_id = thread_id
        self.name = name
        self.counter = counter

    def run(self):
        print(f'Starting {self.name}')
        MyThread.thread_lock.acquire()  # Get lock to synchronize threads
        print_time(self.name, self.counter, 3)
        MyThread.thread_lock.release()  # Free lock to release next thread


def print_time(thread_name, delay, counter):
    while counter:
        time.sleep(delay)
        print(f'{thread_name}: {time.ctime(time.time())}')
        counter -= 1