import time


def pause(t):
    def wrapper(f):
        def tmp(*args, **kwargs):
            time.sleep(t)
            return f(*args, **kwargs)
        return tmp
    return wrapper


@pause(4)  # will wait 4 seconds before starting
def func(x, y):
    return x + y


print(func(56, 78))