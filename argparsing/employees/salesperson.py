from argparsing.employees.employee import Employee
from argparsing.functions.db_funcs import *
from argparsing.functions.functions import *
import logging


class Salesperson(Employee):

    addition_msg = '''Would you like to add an ingredient to your beverage?
    1 - Add ingredient
    2 - Don not add ingredient\n'''

    def __init__(self, name, position, beverage, addition):
        super().__init__(name, position)
        self.beverage = beverage
        self.addition = addition
        self.logger = logging.getLogger('main.argparsing.employees.Salesperson')
        self.logger.debug('Initialising  Salesperson')

    def create_employee(self, args):
        self.logger.debug('create_employee(): creating Salesperson employee')
        print('Hi {}! You are a {}.\nYou can sell the following beverages:'.format(args.name[0], args.position[0]))
        for beverage in args.beverage:
            print(Colors.GREEN + beverage + Colors.RESET)
        self.logger.info('create_employee(): created Salesperson employee: {}'.format(self.__str__()))
        return Salesperson(args.name[0], args.position[0], args.beverage, args.addition)

    def add_beverage(self, available_beverages):
        while True:
            beverage_to_sell = get_item_to_sell('beverage', available_beverages)
            if beverage_to_sell.lower() in [x.lower() for x in available_beverages]:
                beverage_price = enter_price('beverage')
                sale_record = 'Beverage: {}. Price: {}$'.format(beverage_to_sell, str(beverage_price))
                self.logger.info('{} added a beverage: {} at {}$'.
                                 format(self.fullname, beverage_to_sell, str(beverage_price)))
                return sale_record
            else:
                self.logger.debug('{} entered incorrect beverage name: {}'.format(self.fullname, beverage_to_sell))
                print('You can sell only:')
                print(' or '.join(Colors.RED + x + Colors.RESET for x in available_beverages))
                print(Colors.BLUE + 'Try again!' + Colors.RESET + '\n')

    def add_ingredient(self, available_additions):
        while True:
            addition_to_sell = get_item_to_sell('ingredient', available_additions)
            if addition_to_sell.lower() in [addition.lower() for addition in available_additions]:
                addition_price = enter_price('ingredient')
                sale_record = 'Addition: {}. Price: {}$'.format(addition_to_sell, str(addition_price))
                self.logger.info('{} added addition: {} at {}$'.
                                 format(self.fullname, addition_to_sell, str(addition_price)))
                return sale_record
            else:
                self.logger.debug('{} entered incorrect addition name: {}'.format(self.fullname, addition_to_sell))
                print('You can add only:')
                print(' or '.join(Colors.RED + addition + Colors.RESET for addition in available_additions))
                print(Colors.BLUE + 'Try again!' + Colors.RESET + '\n')

    def make_sale(self, available_beverages, available_additions):
        if self.user_choice(self.addition_msg, 3) == 2:
            self.logger.debug('{} decided not to add additions to sale'.format(self.fullname))
            beverage_to_file(employee_filename(self.fullname), self.add_beverage(available_beverages))
            self.logger.info('{} added beverage to file'.format(self.fullname))
            if is_employee_in_db(self.fullname):
                update(self.fullname, self.count_sales(), self.total_sales_amount())
                self.logger.info('Sales and total amount were updated for {} in db'.format(self.fullname))
            else:
                insert(self.fullname, self.count_sales(), self.total_sales_amount())
                self.logger.info('{} was added to db'.format(self.fullname))
        else:
            self.logger.debug('{} decided to add additions to sale'.format(self.fullname))
            beverage_addition_to_file(employee_filename(self.fullname),
                                      self.add_beverage(available_beverages), self.add_ingredient(available_additions))
            self.logger.info('{} added addition to file'.format(self.fullname))
            if is_employee_in_db(self.fullname):
                update(self.fullname, self.count_sales(), self.total_sales_amount())
                self.logger.info('Sales and total amount were updated for {} in db'.format(self.fullname))
            else:
                insert(self.fullname, self.count_sales(), self.total_sales_amount())
                self.logger.info('{} was added to db'.format(self.fullname))

    def total_sales_amount(self):
        try:
            with open(employee_filename(self.fullname), "r") as f:
                total_price = []
                for line in f:
                    try:
                        match_price(total_price, r'[-+]?\d*\.\d+|\d+', line)
                    except IndexError as e:
                        self.logger.error('Sale price is missing in {} line --> {}'.format(line, e))
                total_price = round(sum(total_price), 2)
                print('Your sales total amount: {}$'.format(total_price))
                self.logger.info('Total sales amount calculated: {}'.format(total_price))
                return total_price
        except TypeError as e:
            self.logger.error('Invalid filename/directory or no file passed... ', e)

    def count_sales(self):
        try:
            with open(employee_filename(self.fullname), 'r') as f:
                contents = f.read()
                beverage_counter = contents.count('Beverage')
                addition_counter = contents.count('Addition')
                print('You sold {} beverages and {} additions'.format(beverage_counter, addition_counter))
                self.logger.info('{} beverages and {} additions added to {} sales file'.
                                 format(str(beverage_counter), str(addition_counter), self.fullname))
                return beverage_counter + addition_counter
        except TypeError as e:
            self.logger.error('Invalid filename/directory or no file passed... ', e)

    def view_records(self):
        try:
            with open(employee_filename(self.fullname), "r") as f:
                self.logger.debug('salesperson.view_records(): printing {} sales records'.format(self.fullname))
                for line in f:
                    print(line)
        except TypeError as e:
            self.logger.error('Invalid filename/directory or no file passed... ', e)

    def __str__(self):
        return '{} - {} - beverages -> {}, additions -> {}'.\
            format(self.name, self.position, self.beverage, self.addition)
