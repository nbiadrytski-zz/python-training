from argparsing.manager import Manager
from argparsing.salesperson import Salesperson
from argparsing.argument_parser import ArgumentParser
from argparsing.functions import *
# Koly2a3 Salesperson -bev=Water -bev=Soda -add=Sugar -add=Salt


def main():
    salesperson_choice_msg = '''What would you like to do? Enter 1 or 2:
    1 - Sell a beverage
    2 - I am tired... No more sales...\n'''
    args = ArgumentParser.parse_arguments()

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
            while ask_user(salesperson_choice_msg) == 'yes':
                salesperson.make_sale(args.beverage, args.addition)
                salesperson.view_records()
                salesperson.count_sales()
                salesperson.total_sales_amount()
            else:
                print('Bye-Bye, {}! See you next time'.format(args.name[0]))
        except NameError as e:
            print('Non-salesperson object: '.format(e))
    else:
        args_positions = ArgumentParser()
        args_positions.quit_msg(args.name[0], args.position[0])


if __name__ == "__main__":
    main()
