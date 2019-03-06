import time


def timer(f):
    def tmp(*args, **kwargs):
        start_time = time.time()
        res = f(*args, **kwargs)  # put function which will be decorated
        print(f'Function execution time: {time.time() - start_time}')
        return res
    return tmp


@timer
def func(x, y):  # instead of func put tmp
    return x + y


func(4, 89)