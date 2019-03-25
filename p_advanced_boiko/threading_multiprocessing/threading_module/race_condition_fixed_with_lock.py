import threading


x = 0  # global var


def increment():  # function to increment global variable x
    global x
    x += 1


# In the critical section of target function, we apply lock using lock.acquire() method.
# As soon as a lock is acquired, no other thread can access the critical section
# (here, increment function) until the lock is released using lock.release() method
def thread_task(lock):
    for _ in range(100000):
        lock.acquire()
        increment()
        lock.release()


def main_task():
    global x
    x = 0

    lock = threading.Lock()

    t1 = threading.Thread(target=thread_task, args=(lock,))
    t2 = threading.Thread(target=thread_task, args=(lock,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()


if __name__ == "__main__":
    for i in range(10):
        main_task()
        print(f'Iteration {i}: x = {x}')

# Iteration 0: x = 200000
# Iteration 1: x = 200000
# Iteration 2: x = 200000
# Iteration 3: x = 200000
# Iteration 4: x = 200000
# Iteration 5: x = 200000
# Iteration 6: x = 200000
# Iteration 7: x = 200000
# Iteration 8: x = 200000
# Iteration 9: x = 200000
