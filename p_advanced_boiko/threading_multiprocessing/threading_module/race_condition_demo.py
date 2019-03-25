import threading


x = 0  # global var
# The expected final value of x is 200000
# but what we get in 10 iterations of main_task function is some different values.
# This happens due to concurrent access of threads to the shared variable x.
# This unpredictability in value of x is nothing but race condition


def increment():  # function to increment global variable x
    global x
    x += 1


def thread_task():
    for _ in range(100000):
        increment()


def main_task():
    global x
    x = 0

    t1 = threading.Thread(target=thread_task)
    t2 = threading.Thread(target=thread_task)

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
# Iteration 2: x = 180104
# Iteration 3: x = 200000
# Iteration 4: x = 200000
# Iteration 5: x = 200000
# Iteration 6: x = 200000
# Iteration 7: x = 177314
# Iteration 8: x = 200000
# Iteration 9: x = 181696
