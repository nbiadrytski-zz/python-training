from argparsing.functions.db_funcs import *
import json
import csv

logger = logging.getLogger('main.argparsing.exporter.exporter.Exporter')


class Exporter:

    @staticmethod
    def export_as_json(file_name):
        try:
            with open(file_name, "w") as f:
                conn = create_connection()
                cur = conn.cursor()
                result = cur.execute('SELECT * FROM ' + table_name)
                items = [dict(zip([key[0] for key in cur.description], row)) for row in result]
                json_records = (json.dumps({table_name: items}))
                logger.debug('export_as_json(): json records to export: {}'.format(json_records))
                f.write(json_records)
                return json_records
        except IOError as e:
            logger.error('File {} not found or path is incorrect... {}'.format(file_name, e))

    @staticmethod
    def export_as_xml(file_name):
        try:
            with open(file_name, "w") as f:
                conn = create_connection()
                cur = conn.cursor()
                cur.execute('SELECT * FROM ' + table_name)
                rows = cur.fetchall()
                f.write('<?xml version="1.0" ?>\n')
                f.write('<employees>\n')
                for row in rows:
                    f.write('  <row>\n')
                    f.write('    <id>%s</id>\n' % row[0])
                    f.write('    <name>%s</name>\n' % row[1])
                    f.write('    <sales>%s</sales>\n' % row[2])
                    f.write('    <amount>%s</amount>\n' % row[3])
                    f.write('  </row>\n')
                f.write('</employees>\n')
                logger.debug('export_as_xml(): stored sales records to xml {} file'.format(file_name))
                conn.close()
        except IOError as e:
            logger.error('File {} not found or path is incorrect... {}'.format(file_name, e))

    @staticmethod
    def export_as_csv(file_name):
        conn = create_connection()
        cur = conn.cursor()
        cur.execute('SELECT * FROM ' + table_name)
        try:
            with open(file_name, 'w') as f:
                writer = csv.writer(f)
                writer.writerow(["ID", "Name", 'Number of Sales', 'Total Amount ($)'])
                for row in cur:
                    writer.writerow(row)
                logger.debug('export_as_csv(): stored sales records to csv {} file'.format(file_name))
        except IOError as e:
            logger.error('File {} not found or path is incorrect... {}'.format(file_name, e))
