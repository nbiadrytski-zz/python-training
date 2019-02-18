from argparsing.employees.employee import Employee
from argparsing.functions.db_funcs import *
from argparsing.exporter.exporter import Exporter
from argparsing.functions.functions import show_sales_table
import logging


class Manager(Employee):

    manager_export_msg = '''Would you like to export sales records? Enter 1, 2, 3 or 4:
        1 - Export as JSON
        2 - Export as XML
        3 - Export as CSV
        4 - Do not export\n'''

    def __init__(self, name, position):
        super().__init__(name, position)
        self.logger = logging.getLogger('main.argparsing.employees.Manager')
        self.logger.debug('Initialising Manager')

    def create_employee(self, args):
        self.logger.debug('create_employee(): creating Manager employee')
        print('Hi {}! You are a {}.\nYou can view all sales records\n'.format(args.name[0], args.position[0]))
        self.logger.info('create_employee(): created Manager employee: {}'.format(self.__str__()))
        return Manager(args.name[0], args.position[0])

    def view_records(self):
        try:
            employees = view_db_records()
            self.logger.debug('{} view_records(): printing salespeople sales records table'.format(self.__str__()))
            show_sales_table(employees)
            self.logger.info('{} viewed the table with sales records'.format(self.__str__()))
        except TypeError:
            print('\nNo sales records yet. Ask your salespeople to sell something.')
            self.logger.info('manager.view_records(): no sales records yet')

    def export_records(self):
        choice = self.user_choice(self.manager_export_msg, 5)
        if choice == 1:
            self.logger.debug('{} is trying to export json records'.format(self.fullname))
            Exporter.export_as_json((self.fullname + '_records.json'))
            self.logger.info('{} exported json records'.format(self.fullname))
            print('{}, you have successfully exported sales records as JSON file\n'.format(self.name))
        elif choice == 2:
            self.logger.debug('{} is trying to export xml records'.format(self.fullname))
            Exporter.export_as_xml(self.fullname + '_records.xml')
            self.logger.info('{} exported xml records'.format(self.fullname))
            print('{}, you have successfully exported sales records as XML file\n'.format(self.name))
        elif choice == 3:
            self.logger.debug('{} is trying to export csv records'.format(self.fullname))
            Exporter.export_as_csv(self.fullname + '_records.csv')
            self.logger.info('{} exported csv records'.format(self.fullname))
            print('{}, you have successfully exported sales records as CSV file\n'.format(self.name))
        elif choice == 4:
            print('{}, you can always export sales records later.\n'.format(self.name))

    def __str__(self):
        return '{} - {}'.format(self.name, self.position)





