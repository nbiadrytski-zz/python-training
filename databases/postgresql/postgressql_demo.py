import psycopg2


conn_details = "dbname='python_training' user='mikalai_biadrytski' host='localhost' port='5432'"


def create_table():
    conn = psycopg2.connect(conn_details)
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()


def insert(item, quantity, price):
    conn = psycopg2.connect(conn_details)
    cur = conn.cursor()
    cur.execute("INSERT INTO store VALUES (%s,%s,%s)", (item, quantity, price))
    conn.commit()
    conn.close()


def view():
    conn = psycopg2.connect(conn_details)
    cur = conn.cursor()
    cur.execute("SELECT * FROM store;")
    rows = cur.fetchall()
    conn.close()
    return print(rows)


def delete(item):
    conn = psycopg2.connect(conn_details)
    cur = conn.cursor()
    cur.execute("DELETE FROM store WHERE item=%s", (item,))
    conn.commit()
    conn.close()


def update(quantity, price, item):
    conn = psycopg2.connect(conn_details)
    cur = conn.cursor()
    cur.execute("UPDATE store SET quantity=%s, price=%s WHERE item=%s", (quantity, price, item))
    conn.commit()
    conn.close()


create_table()
update(100, 23.8, "Orange")
# insert("Pineapple",13,1549)
# delete("Apple")
view()
