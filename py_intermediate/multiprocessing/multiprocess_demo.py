import multiprocessing

'''Since Python doesn't allow to use  > about 16% of core cpu,
use multiprocessing module to use all your cpu'''


def spawn(num, num2):
    print('Spawned! {} {}'.format(num, num2))


if __name__ == '__main__':
    for i in range(55):
        p = multiprocessing.Process(target=spawn, args=(i, 1+1))
        p.start()
        p.join()  # wait for the process to complete
