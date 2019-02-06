import sys
import os
import random
import datetime


def main():
    v = sys.version_info
    print('Python version {}.{}.{}'.format(*v))  # Python version 3.6.4

    print(sys.platform)  # darwin

    print(os.name)  # posix

    print(os.getenv('PATH'))

    print(os.getcwd())  # pwd

    print(random.randint(1, 1000))

    x = list(range(25))
    random.shuffle(x)
    print(x)

    now = datetime.datetime.now()
    print(now.year, now.month, now.year, now.day, now.hour, now.minute, now.second)


if __name__ == '__main__':
    main()
