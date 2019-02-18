import sqlite3
import logging

db_name = 'employees.db'
table_name = 'employees'

logger = logging.getLogger('main.argparsing.functions.db_funcs')


def create_connection():
    try:
        conn = sqlite3.connect(db_name)
        logger.debug('create_connection(): created connection to {}'.format(db_name))
        return conn
    except sqlite3.Error as e:
        logger.error('create_connection(): could not create connection... {}'.format(e))
    return None


def create_table():
    conn = create_connection()
    try:
        cur = conn.cursor()
        cur.execute(
            'CREATE TABLE IF NOT EXISTS ' + table_name +
            ' (id INTEGER PRIMARY KEY, name text, sales integer, amount integer)')
        conn.commit()
        logger.debug('create_table(): created {} if not exists already'.format(table_name))
    except sqlite3.Error as e:
        logger.error('create_table(): could not create table {}... {}'.format(table_name, e))
    finally:
        conn.close()


def is_employee_in_db(name):
    conn = create_connection()
    try:
        cur = conn.cursor()
        cur.execute('SELECT * FROM ' + table_name + ' WHERE name=?', (name,))
        row = cur.fetchall()
        if name in [i[1] for i in row]:
            logger.debug('is_employee_in_db(): {} is found in {} table'.format(name, table_name))
            return True
        else:
            logger.debug('is_employee_in_db(): {} is not found in {} table'.format(name, table_name))
            return False
    except sqlite3.Error as e:
        logger.error('is_employee_in_db: error when fetching employee from table... {}'.format(e))
    finally:
        conn.close()


def insert(name, sales, amount):
    conn = create_connection()
    try:
        cur = conn.cursor()
        # NULL will be replaced by id
        cur.execute('INSERT INTO ' + table_name + ' VALUES (NULL,?,?,?)', (name, sales, amount))
        conn.commit()
        logger.debug('insert(): {} was added to {} table'.format(name, table_name))
    except sqlite3.Error as e:
        logger.error('insert(): error when inserting employee {} into {} table... {}'.format(name, table_name, e))
    finally:
        conn.close()


def update(name, sales, amount):
    conn = create_connection()
    try:
        cur = conn.cursor()
        cur.execute('UPDATE ' + table_name + ' SET amount=?, sales=? WHERE name=?', (amount, sales, name))
        conn.commit()
        logger.debug('update(): {} record was updated in {} table with {} sales and {} amount'.
                     format(name, table_name, sales, amount))
    except sqlite3.Error as e:
        logger.error('update(): error updating {} record in {} table with {} sales and {} amount... {}'.
                     format(name, table_name, sales, amount, e))
    finally:
        conn.close()


def view_db_records():
    conn = create_connection()
    try:
        cur = conn.cursor()
        cur.execute('SELECT * FROM ' + table_name)
        rows = cur.fetchall()
        logger.debug('view_db_records(): selected all salespeople records from {} table'.format(table_name))
        return rows
    except sqlite3.Error as e:
        logger.error('view_db_records(): Error when viewing employee records in {} table... {}'.format(table_name, e))
    finally:
        conn.close()


def is_table_empty():
    conn = create_connection()
    try:
        cur = conn.cursor()
        cur.execute('SELECT * FROM ' + table_name)
        rows = cur.fetchall()
        logger.debug('is_table_empty(): selected all salespeople records from {} table'.format(table_name))
        if not rows:
            print('There are no sales records. Ask your salespeople to sell something...\n')
            logger.info('is_table_empty(): there are no sales records in {} table yet'.format(table_name))
            return True
    except sqlite3.Error as e:
        logger.error('is_table_empty(): unable to select from {}...'.format(table_name, e))
    finally:
        conn.close()
    return False







