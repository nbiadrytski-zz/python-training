import argparse
from argparsing.manager import Manager
from argparsing.salesperson import Salesperson
# https://www.geeksforgeeks.org/command-line-interface-programming-python/


def is_manager(args):
    if args.position[0].lower() == 'manager':
        return True


def is_salesperson(args):
    if args.position[0].lower() == 'salesperson':
        return True


def create_manager(args):
    print('Hi {}! You are a {}'.format(args.name[0], args.position[0]))
    return Manager(args.name[0], args.position[0])


def create_salesperson(args):
    print('Hi {}! You are a {}'.format(args.name[0], args.position[0]))
    return Salesperson(args.name[0], args.position[0])


def main():
    global manager
    global salesperson
    global owner

    parser = argparse.ArgumentParser(description="Buy drinks and view records with Coffee App!",
                                     prog='Coffee CLI App-->',
                                     epilog='Thank you for using Coffee CLI App!')
    # parser.add_argument("-p", "--position", type=str, nargs=1, metavar="employee_position", default=None,
    #                    help="Employee position")
    parser.add_argument('name', type=str, nargs=1, metavar='employee_name', default=None,
                        help='Employee name')
    parser.add_argument('position', type=str, nargs=1, metavar='employee_position', default=None,
                        help='Employee position')

    args = parser.parse_args()

    # if args.position is not None:
    if is_manager(args):
        try:
            manager = create_manager(args)
            manager.view_records()
        except NameError as e:
            print('Non-manager object: ', e)

    elif is_salesperson(args):
        try:
            salesperson = create_salesperson(args)
            salesperson.make_sale()
        except NameError as e:
            print('Non-salesperson object: ', e)

    else:
        print('"{}" with "{}" position is not a valid employee'.format(args.name[0], args.position[0]))


if __name__ == "__main__":
    main()
