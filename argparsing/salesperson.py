from argparsing.employee import Employee
from argparsing.functions import *


class Salesperson(Employee):

    def __init__(self, name, position, beverage):
        super().__init__(name, position)
        self.beverage = beverage

    def create_employee(self, args):
        print('Hi {}! You are a {}'.format(args.name[0], args.position[0]))
        print('You can sell the following beverages: {}'.format(args.beverage))
        return Salesperson(args.name[0], args.position[0], args.beverage)

    def make_sale(self, available_beverages):
        decide = input('Would you like to sell a beverage? Enter yes or no: ')
        if decide == 'yes':
            beverage_to_sell = input('Which beverage will you sell?: {}'.format(available_beverages))
            beverage_price = input('Enter price: ')
            sale_record = 'Beverage: {}. Price: {}$'.format(beverage_to_sell, str(beverage_price))
            filename = self.fullname + '_records.txt'
            save_sale_to_file(filename, sale_record)
            return filename
        else:
            print('Bye!')
            return None

    def view_records(self, file):
        try:
            with open(file, "r") as f:
                salesperson_records(f)
        except TypeError as e:
            print('Invalid filename or no file passed... ', e)



