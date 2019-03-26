from multiprocessing import Process
from multiprocessing.sharedctypes import Value, Array


def f(n, a):
    n.value = 3.1415927
    for i in range(len(a)):
        a[i] = -a[i]


if __name__ == '__main__':
    num = Value('d', 0.0)  # d (double) defines type of data in this shared memory
    arr = Array('i', range(10))
    print(arr[:])

    p = Process(target=f, args=(num, arr))  # create child process (parent is main process)
    p.start()
    p.join()  # wait until child Process finishes working on f()

    print(num.value)
    print(arr[:])