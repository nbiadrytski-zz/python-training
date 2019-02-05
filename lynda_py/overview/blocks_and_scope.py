#!/usr/bin/env python3


def main():
    x = 42
    y = 73

    if x < y:
        print('x < y: x is {} and y is {}'.format(x, y))
    elif x > y:
        print('This is elif')
    else:
        print('This is else')


if __name__ == '__main__':
    main()
