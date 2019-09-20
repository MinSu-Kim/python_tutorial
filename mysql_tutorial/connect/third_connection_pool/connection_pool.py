from mysql.connector.pooling import MySQLConnectionPool
from mysql_tutorial.connect.second.python_mysql_dbconfig import read_db_config


class DatabaseConnectionPool(object):
    INSTANCE = None

    def __init__(self):
        if self.INSTANCE is not None:
            raise ValueError("An instantiation already exists!")
        else:
            db_config = read_db_config()
            self.__cnxPool = MySQLConnectionPool(pool_name="myPool", **db_config)

    @classmethod
    def get_instance(cls):
        if cls.INSTANCE is None:
            cls.INSTANCE = DatabaseConnectionPool()
        return cls.INSTANCE;

    def get_connection(self):
        return self.__cnxPool.get_connection()


if __name__ == '__main__':
    connection = DatabaseConnectionPool.get_instance().get_connection()
    cursor = connection.cursor()
    cursor.execute("select * from product")
    rows = cursor.fetchall()

    print('Total Row(s):', cursor.rowcount)
    for row in rows:
        print(type(row), " => ",  row)

    connection.close()
