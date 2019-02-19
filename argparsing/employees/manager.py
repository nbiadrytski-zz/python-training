from argparsing.employees.employee import Employee
from argparsing.functions.db_funcs import *
from argparsing.exporter.exporter import Exporter
from argparsing.functions.functions import show_sales_table, employee_filename
from argparsing.functions.colors import Colors
import logging


class Manager(Employee):
    """
    Manager class inherits Employee class.
    Holds logic for viewing salespeople sales records in formatted table
    And exporting sales records to different formats.

    Attributes:
        name (str): Manager first name passed as a command line argument
        position (str): Manager position passed as a command line argument
        logger (Logger): creating Logger for Manager class
    """

    manager_export_msg = '''Would you like to export sales records? Enter 1, 2, 3 or 4:
        1 - Export as JSON
        2 - Export as XML
        3 - Export as CSV
        4 - Do not export\n'''

    def __init__(self, name, position):
        """
        The constructor for Manager class.

        Attributes:
            name (str): Manager first name
            position (str): Manager as position
        """
        super().__init__(name, position)
        self.logger = logging.getLogger('main.argparsing.employees.Manager')

    def create_employee(self, args):
        """
        Creates Manager instance. Overrides Employee.create_employee() method.
        Prints greeting message to Manager.

        Parameters:
            args (argparse.Namespace): Arguments passed via command line.

        Returns:
            Manager: name and position.
        """
        self.logger.debug('create_employee(): creating Manager employee')
        print('Hi {}! You are a {}.\nYou can view all sales records\n'.
              format(Colors.GREEN + args.name[0] + Colors.RESET, args.position[0]))
        self.logger.info('create_employee(): created Manager employee: {}'.format(self.__str__()))
        return Manager(args.name[0], args.position[0])

    def view_records(self):
        """
        Printing salespeople sales records stored in database in formatted table.
        Overrides Employee.view_records() method.

        Raises:
            RuntimeWarning: If no records found in database.
        """
        try:
            employees = view_db_records()
            self.logger.debug('{} view_records(): printing salespeople sales records table'.format(self.__str__()))
            show_sales_table(employees)
            self.logger.info('{} viewed the table with sales records'.format(self.__str__()))
        except RuntimeWarning:
            print('\nNo sales records yet. Ask your salespeople to sell something.\n')
            self.logger.info('manager.view_records(): no sales records yet')

    def export_records(self):
        """
        Exporting sales records to json, xml and csv files based on user's choice.
        Informing user that the export was successful.
        """
        choice = self.user_choice(self.manager_export_msg, 5)
        if choice == 1:
            self.logger.debug('{} is trying to export json records'.format(self.fullname))
            Exporter.export_as_json(employee_filename('manager_records', self.fullname, '_records.json'))
            self.logger.info('{} exported json records'.format(self.fullname))
            print('{}, you successfully exported sales records as JSON file stored in "manager_records" subfolder\n'.
                  format(self.name))
        elif choice == 2:
            self.logger.debug('{} is trying to export xml records'.format(self.fullname))
            Exporter.export_as_xml(employee_filename('manager_records', self.fullname, '_records.xml'))
            self.logger.info('{} exported xml records'.format(self.fullname))
            print('{}, you successfully exported sales records as XML file stored in "manager_records" subfolder\n'.
                  format(self.name))
        elif choice == 3:
            self.logger.debug('{} is trying to export csv records'.format(self.fullname))
            Exporter.export_as_csv(employee_filename('manager_records', self.fullname, '_records.csv'))
            self.logger.info('{} exported csv records'.format(self.fullname))
            print('{}, you have exported sales records as CSV file stored in "manager_records" subfolder\n'.
                  format(self.name))
        elif choice == 4:
            print('{}, you can always export sales records later.\n'.format(self.name))

    def __str__(self):
        return '{} - {}'.format(self.name, self.position)
