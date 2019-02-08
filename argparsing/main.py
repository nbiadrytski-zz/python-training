from argparsing.manager import Manager
from argparsing.salesperson import Salesperson
from argparsing.argument_parser import ArgumentParser
from argparsing.functions import *
# https://www.geeksforgeeks.org/command-line-interface-programming-python/
# Lola Salesperson -bev=Water -bev=Soda


def main():
    args = ArgumentParser.parse_arguments()

    # if args.position is not None:
    if is_manager(args):
        try:
            manager = Manager(args.name[0], args.position[0])
            manager.create_employee(args)
            manager.view_records()
        except NameError as e:
            print('Non-manager object: {}'.format(e))

    elif is_salesperson(args):
        try:
            salesperson = Salesperson(args.name[0], args.position[0], args.beverage)
            salesperson.create_employee(args)
            record = salesperson.make_sale(args.beverage)
            if record is not None:
                salesperson.view_records(record)
        except NameError as e:
            print('Non-salesperson object: '.format(e))
    else:
        print('"{}" with "{}" position is not a valid employee'.format(args.name[0], args.position[0]))


if __name__ == "__main__":
    main()
