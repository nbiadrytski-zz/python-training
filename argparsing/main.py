import argparse
from argparsing.manager import Manager
from argparsing.salesperson import Salesperson


# https://www.geeksforgeeks.org/command-line-interface-programming-python/
# Lola Salesperson -bev=Water -bev=Soda


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
    print('You can sell the following beverages: {}'.format(args.beverage))
    return Salesperson(args.name[0], args.position[0], args.beverage)


def main():
    global manager
    global salesperson

    parser = argparse.ArgumentParser(description="Buy drinks and view records with Coffee App!",
                                     prog='Coffee CLI App-->',
                                     epilog='Thank you for using Coffee CLI App!')

    parser.add_argument('name', type=str, nargs=1, metavar='employee_name', default=None,
                        help='Employee name')
    parser.add_argument('position', type=str, nargs=1, metavar='employee_position', default=None,
                        help='Employee position')
    parser.add_argument("-bev", "--beverage", action='append', default=None,
                        help="List of available beverages: tea, coffee, water, soda, milk, etc.")
    parser.add_argument("-add", "--addition", type=str, default=None,
                        help="List of available beverage additions: sugar, milk, cinnamon, etc. ")

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
            record = salesperson.make_sale(args.beverage)
            if record is not None:
                salesperson.view_records(record)
        except NameError as e:
            print('Non-salesperson object: ', e)

    else:
        print('"{}" with "{}" position is not a valid employee'.format(args.name[0], args.position[0]))


if __name__ == "__main__":
    main()
