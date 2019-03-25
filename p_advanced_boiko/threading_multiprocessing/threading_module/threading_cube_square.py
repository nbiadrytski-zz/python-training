import threading


def print_cube(num):
    print(f'Cube: {num * num * num}')


def print_square(num):
    print(f'Square: {num * num}')


if __name__ == '__main__':
    t1 = threading.Thread(target=print_square, args=(10,))
    t2 = threading.Thread(target=print_cube, args=(10,))

    t1.start()
    t2.start()

    # current program (you can think of it like a main thread) will first wait for the completion of t1 and then t2.
    # Once, they are finished, the remaining statements of current program are executed.
    t1.join()
    t2.join()

    print('Done')