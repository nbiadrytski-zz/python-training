#!/usr/bin/env python3


def main():
    words = ['one', 'two', 'three']

    n = 0

    while n < 3:
        print(words[n])
        n += 1

    # fibonacci numbers
    a, b = 0, 1
    while b < 1000:
        print(b, end=' ', flush=True)
        a, b = b, a + b
    print('\n')

    for i in words:
        print(i)


if __name__ == '__main__':
    main()
