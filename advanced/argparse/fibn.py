import argparse


# run as "python3 fibn.py 10"
# to see help run as "python3 fibn.py -h"
# to save result in file run as "python3 fibn.py 10 -o"
# to get verbose output run as "python3 fibn.py 10 -v"
# to get quiet output run as "python3 fibn.py 10 -v"


def fib(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a


def main():
    parser = argparse.ArgumentParser()

    group = parser.add_mutually_exclusive_group()
    group.add_argument("-v", "--verbose", action="store_true")
    group.add_argument("-q", "--quiet", action="store_true")

    parser.add_argument("num", help="The Fibonacci number " +
                                    "you wish to calculate.", type=int)
    parser.add_argument("-o", "--output", help="Output the " + \
                                               "result to a file", action="store_true")
    args = parser.parse_args()

    result = fib(args.num)
    if args.verbose:
        print("The " + str(args.num) + "th fib number is " + str(result))
    elif args.quiet:
        print(result)
    else:
        print("Fib(" + str(args.num) + ") = " + str(result))

    if args.output:
        f = open("fibonacci.txt", "a")
        f.write(str(result) + "\n")


if __name__ == '__main__':
    main()


'''$ python3 fibn.py -h
usage: fibn.py [-h] [-v | -q] [-o] num

positional arguments:
  num            The Fibonacci number you wish to calculate.

optional arguments:
  -h, --help     show this help message and exit
  -v, --verbose
  -q, --quiet
  -o, --output   Output the result to a file'''
