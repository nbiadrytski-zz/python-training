import argparse
from argparsing.manager import Manager

# https://www.geeksforgeeks.org/command-line-interface-programming-python/


def is_manager(args):
    if args.position[0] == 'Manager':
        return True
    elif args.position[0] == 'Salesperson':
        return False


def manager_options(args):
    print('Hi {}! You are a {}'.format(args.name[0], args.position[0]))
    if is_manager(args):
        man = Manager(args.name[0])
        man.view_records()


def main():
    parser = argparse.ArgumentParser(description="Coffee CLI!", prog='jhfjhkvjvjv')

    parser.add_argument("-name", "--name", type=str, nargs=1, metavar="employee_name", default=None,
                        help="Employee name")
    parser.add_argument("-position", "--position", type=str, nargs=1, metavar="employee_position", default=None,
                        help="Employee position")

    args = parser.parse_args()

    if args.position is not None:
        manager_options(args)


if __name__ == "__main__":
    main()
