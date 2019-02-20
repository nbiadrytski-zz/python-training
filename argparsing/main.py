from argparsing.employees.manager import Manager
from argparsing.employees.salesperson import Salesperson
from argparsing.argsparser.argument_parser import ArgumentParser
from argparsing.functions.db_funcs import create_table, is_table_empty
from argparsing.functions.functions import get_employee_position
import logging
# Koly2a3 Salesperson -bev=Water -bev=Soda -add=Sugar -add=Salt


def main():
    logger = logging.getLogger('main')
    logger.setLevel(logging.INFO)
    file_handler = logging.FileHandler('coffee_for_me.log')
    file_handler.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    salesperson_choice_msg = '''What would you like to do? Enter 1 or 2:
    1 - Sell a beverage
    2 - I am tired... No more sales...\n'''

    manager_choice_msg = '''What would you like to do? Enter 1 or 2:
        1 - View/export sales records
        2 - No reports today... Maybe later...\n'''

    parser = ArgumentParser.parse_arguments()
    print('=' * 76)
    parser.print_help()  # printing Help for user once the app is started
    print('=' * 76 + '\n')
    args = parser.parse_args()
    logger.info('User passed the following command line args: {}'.format(args))

    if get_employee_position(args) == 'manager':
        try:
            manager = Manager(args.name[0], args.position[0])
            logger.info('Created Manager instance: {}'.format(manager.__str__()))
            manager.employee_greeting('\nYou can view and export sales records\n')
            logger.debug('Greeted {}'.format(manager.__str__()))
            while manager.user_choice(manager_choice_msg, 3) == 1:
                create_table()
                logger.info('DB table created: {}'.format(manager.fullname))
                if not is_table_empty():
                    manager.view_records()
                    logger.info('{} viewed salespeople records'.format(manager.fullname))
                    manager.export_records()
                    logger.info('{} exported salespeople records'.format(manager.fullname))
            else:
                print('Bye-Bye, {}! See you next time'.format(args.name[0]))
                logger.info('Manager {} decided to quit the app'.format(manager.fullname))
        except NameError:
            logger.error('Non-manager object is trying to access manager stuff...')

    elif get_employee_position(args) == 'salesperson':
        try:
            salesperson = Salesperson(args.name[0], args.position[0], args.beverage, args.addition)
            logger.info('Created Salesperson instance: {}'.format(salesperson.__str__()))
            salesperson.employee_greeting('\nYou can sell beverages and ingredients\n')
            logger.debug('Greeted {}'.format(salesperson.__str__()))
            while salesperson.user_choice(salesperson_choice_msg, 3) == 1:
                create_table()
                logger.info('DB table created: {}'.format(salesperson.fullname))
                salesperson.make_sale(args.beverage, args.addition)
                logger.info('{} made a sale'.format(salesperson.fullname))
                salesperson.view_records()
                logger.info('Salesperson {} is viewing personal sales records'.format(salesperson.fullname))
            else:
                print('Bye-Bye, {}! See you next time'.format(args.name[0]))
                logger.info('Salesperson {} decided to quit the app'.format(salesperson.fullname))
        except NameError:
            logger.error('Non-salesperson object is trying to access salesperson stuff...')
    else:
        args_positions = ArgumentParser()
        args_positions.quit_msg(args.name[0], args.position[0])
        logger.error('{} with position {} is not a valid employee...'.format(args.name[0], args.position[0]))


if __name__ == "__main__":
    main()
