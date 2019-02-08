from argparsing.employee import Employee
from argparsing.functions import *


class Salesperson(Employee):

    def __init__(self, name, position, beverage):
        super().__init__(name)
        self.position = position
        self.beverage = beverage

    def print_beverage(self):
        print('Beverages available now: {}'.format(self.beverage))

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
        read_sale_from_file(file)



