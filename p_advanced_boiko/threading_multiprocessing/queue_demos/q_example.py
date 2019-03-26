from queue import Queue
from threading import Thread


num_worker_threads = 2


def do_work(item):  # simulate work
    s = str(item)
    print(s[::-1])


def worker():
    while True:
        item = q.get()  # get task from queue_demos
        do_work(item)
        q.task_done()  # inform about task completion


def source():  # generate data for queue_demos
    for i in range(100, 105):
        yield i


q = Queue()  # FIFO

for i in range(num_worker_threads):  # create threads
    t = Thread(target=worker)
    t.setDaemon(True)
    t.start()

for item in source():
    q.put(item)

q.join()  # Ставим блокировку до тех пор пока не будут выполнены все задания

