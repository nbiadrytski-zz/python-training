import requests
import threading
from queue import Queue


NUM_WORKER_THREADS = 3


def download_page(page_info):
    """Download and save webpage."""
    r = requests.get(page_info['url'])
    with open(page_info['name'] + '.html', 'w') as save_file:
        save_file.write(r.text)


def handle_tasks(tasks_queue):
    """Monitor tasks queue and execute tasks as appropriate."""
    while True:
        download_page(tasks_queue.get())
        tasks_queue.task_done()


if __name__ == '__main__':
    tasks = Queue(maxsize=0)  # maxsize=0 means infinite size limit

    for i in range(NUM_WORKER_THREADS):  # Create and start worker threads
        worker = threading.Thread(target=handle_tasks, args=(tasks,))
        worker.daemon = True
        worker.start()

    # Add some tasks to the queue
    tasks.put({'name': 'google', 'url': "http://google.com"})
    tasks.put({'name': 'reddit', 'url': "http://reddit.com"})
    tasks.put({'name': 'ebay', 'url': "http://ebay.com"})
    tasks.put({'name': 'bbc', 'url': "http://bbc.co.uk"})

    tasks.join()  # we exit the program when the tasks queue has been fully completed, using the .join() method



