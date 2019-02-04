import argparse
import sys


# run as "python3 cli_argparse.py --x=5 --y=2 --operation=mul"
# run as " python3 cli_argparse.py -h" to see help

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--x', type=float, default=1.0,
                        help='What is the first number?')
    parser.add_argument('--y', type=float, default=1.0,
                        help='What is the second number?')
    parser.add_argument('--operation', type=str, default='add',
                        help='What operation? (add, sub, mul or div)')
    args = parser.parse_args()
    sys.stdout.write(str(calc(args)))


def calc(args):
    if args.operation == 'add':
        return args.x + args.y
    elif args.operation == 'sub':
        return args.x - args.y
    elif args.operation == 'mul':
        return args.x * args.y
    elif args.operation == 'div':
        return args.x / args.y


if __name__ == '__main__':
    main()
    print('\n')
