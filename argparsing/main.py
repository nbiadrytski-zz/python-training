from argparsing.employees.manager import Manager
from argparsing.employees.salesperson import Salesperson
from argparsing.argsparser.argument_parser import ArgumentParser
from argparsing.functions.db_funcs import create_table, is_table_empty
from argparsing.functions.functions import get_employee_position
import logging
# Koly2a3 Salesperson -bev=Water -bev=Soda -add=Sugar -add=Salt


def main():
    logger = logging.getLogger('main')
    logger.setLevel(logging.DEBUG)

    file_handler = logging.FileHandler('cafe.log')
    file_handler.setLevel(logging.DEBUG)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)

    salesperson_choice_msg = '''What would you like to do? Enter 1 or 2:
    1 - Sell a beverage
    2 - I am tired... No more sales...\n'''

    manager_choice_msg = '''What would you like to do? Enter 1 or 2:
        1 - View/export sales records
        2 - No reports today... Maybe later...\n'''

    args = ArgumentParser.parse_arguments()

    if get_employee_position(args) == 'manager':
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
        except NameError:
            print('Non-manager object is trying to access manager stuff...')

    elif get_employee_position(args) == 'salesperson':
        try:
            logger.debug('creating Salesperson instance')
            salesperson = Salesperson(args.name[0], args.position[0], args.beverage, args.addition)
            logger.info('Created salesperson instance: {}'.format(salesperson.__str__()))
            logger.debug('Creating Salesperson employee')
            salesperson.create_employee(args)
            logger.info('Created salesperson employee: {}'.format(salesperson.__str__()))
            while salesperson.user_choice(salesperson_choice_msg, 3) == 1:
                logger.debug('Creating DB table to store salespeople data (salesperson)')
                create_table()
                logger.info('DB table created: {}'.format(salesperson.fullname))
                logger.debug('{} is going to make a sale'.format(salesperson.fullname))
                salesperson.make_sale(args.beverage, args.addition)
                logger.info('{} made a sale'.format(salesperson.fullname))
                salesperson.view_records()
                logger.info('Salesperson {} is viewing personal sales records'.format(salesperson.fullname))
            else:
                print('Bye-Bye, {}! See you next time'.format(args.name[0]))
                logger.info('{} decided to quit the app'.format(salesperson.fullname))
        except NameError:
            logger.error('Non-salesperson object is trying to access salesperson stuff...')
    else:
        args_positions = ArgumentParser()
        args_positions.quit_msg(args.name[0], args.position[0])


if __name__ == "__main__":
    main()
