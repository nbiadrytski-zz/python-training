from postgres.config_provider import ConfigProvider

import psycopg2


class DbManager:
    def __init__(self):
        self.cfg = ConfigProvider()
        self.conn = None
        self.cursor = self.open_connection()

    def open_connection(self):
        self.conn = psycopg2.connect(
            host=self.cfg.get('postgresql', 'host'),
            database=self.cfg.get('postgresql', 'database'),
            user=self.cfg.get('postgresql', 'user'),
            password=self.cfg.get('postgresql', 'password'))
        return self.conn.cursor()

    def execute_query(self, query):
        self.cursor.execute(query)

    def show_query_result(self):
        print(self.cursor.fetchone())

    def close_connection(self):
        if self.conn is not None:
            self.conn.close()


if __name__ == '__main__':
    db_client = DbManager()
    try:
        db_client.execute_query('select * from payment limit 1;')
        db_client.show_query_result()
    finally:
        db_client.close_connection()
