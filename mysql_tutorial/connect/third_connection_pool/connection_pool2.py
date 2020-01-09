import mysql
from mysql.connector.pooling import MySQLConnectionPool


class ExplicitlyConnectionPool(object):
    INSTANCE = None

    def __init__(self):
        if self.INSTANCE is not None:
            raise ValueError("An instantiation already exists!")
        else:
            self.__cnxPool = MySQLConnectionPool(pool_name="myPool", pool_size=5, option_files='config.conf')

    @classmethod
    def get_instance(cls):
        if cls.INSTANCE is None:
            cls.INSTANCE = ExplicitlyConnectionPool()
        return cls.INSTANCE;

    def get_connection(self):
        return self.__cnxPool.get_connection()


def get_implicitly_connection():
    return mysql.connector.connect(option_files='config.conf', pool_name="myPool", pool_size=5)


