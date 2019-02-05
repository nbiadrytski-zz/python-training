#!/usr/bin/env python3
import platform


def main():
    message()
    another_message()


def message():
    print('This is Python version {}'.format(platform.python_version()))


def another_message():
    x = 42
    print(f'Hello, World {x}')


if __name__ == '__main__':
    main()
