from multiprocessing import Process, current_process
from threading import Thread, currentThread
import time


def say_hello():
    thread_name = currentThread().name
    process_name = current_process().name
    print(f'Hello {thread_name} {process_name}')
    time.sleep(2)


jobs = [Process(target=say_hello, name=f'Proc_{i}') for i in range(5)]

jobs = jobs+[Thread(target=say_hello, name=f'Thread_{i}') for i in range(5)]

for job in jobs:
    job.start()

for job in jobs:
    job.join()