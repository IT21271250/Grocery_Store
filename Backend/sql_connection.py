import mysql.connector

__connect = None

def get_sql_connection():
    global __connect
    if __connect is None:
        __connect = mysql.connector.connect(host='localhost', database='grocery_store', user='root',password='root')

    return __connect