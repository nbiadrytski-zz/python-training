from argparsing.manager import Manager
from argparsing.salesperson import Salesperson
from argparsing.argument_parser import ArgumentParser
from argparsing.functions import *
from argparsing.db_funcs import create_table, is_table_empty
# Koly2a3 Salesperson -bev=Water -bev=Soda -add=Sugar -add=Salt


def main():
    salesperson_choice_msg = '''What would you like to do? Enter 1 or 2:
    1 - Sell a beverage
    2 - I am tired... No more sales...\n'''

    manager_choice_msg = '''What would you like to do? Enter 1 or 2:
        1 - View/export sales records
        2 - No reports today... Maybe later...\n'''

    args = ArgumentParser.parse_arguments()

    if is_manager(args):
        try:
            manager = Manager(args.name[0], args.position[0])
            manager.create_employee(args)
            while manager.user_choice(manager_choice_msg, 3) == 1:
                create_table()
                if not is_table_empty():
                    manager.view_records()
                    manager.export_records()
            else:
                print('Bye-Bye, {}! See you next time'.format(args.name[0]))
        except NameError as e:
            print('Non-manager object: {}'.format(e))

    elif is_salesperson(args):
        try:
            salesperson = Salesperson(args.name[0], args.position[0], args.beverage)
            salesperson.create_employee(args)
            while salesperson.user_choice(salesperson_choice_msg, 3) == 1:
                create_table()
                salesperson.make_sale(args.beverage, args.addition)
                salesperson.view_records()
            else:
                print('Bye-Bye, {}! See you next time'.format(args.name[0]))
        except NameError as e:
            print('Non-salesperson object: '.format(e))
    else:
        args_positions = ArgumentParser()
        args_positions.quit_msg(args.name[0], args.position[0])


if __name__ == "__main__":
    main()
