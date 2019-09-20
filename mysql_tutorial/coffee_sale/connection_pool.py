from mysql.connector.pooling import MySQLConnectionPool
from mysql_tutorial.connect.second.python_mysql_dbconfig import read_db_config


class DatabaseConnectionPool(object):
    INSTANCE = None

    def __init__(self):
        if self.INSTANCE is not None:
            raise ValueError("An instantiation already exists!")
        else:
            db_config = read_db_config()
            self.__cnxPool = MySQLConnectionPool(pool_name="myPool", pool_size=5, **db_config)

    @classmethod
    def get_instance(cls):
        if cls.INSTANCE is None:
            cls.INSTANCE = DatabaseConnectionPool()
        return cls.INSTANCE;

    def get_connection(self):
        return self.__cnxPool.get_connection()


