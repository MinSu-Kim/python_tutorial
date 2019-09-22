import mysql
from mysql.connector import errorcode

from mysql_tutorial.connect.third_connection_pool.connection_pool import DatabaseConnectionPool
from mysql_tutorial.ddl_query.read_config import read_db_config


class DbInit:
    def __init__(self):
        self._db = read_db_config()

    def create_database(self):
        try:
            sql = read_db_config()
            conn = DatabaseConnectionPool.get_instance().get_connection()
            cursor = conn.cursor()
            cursor.execute("CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(self._db['database_name']))
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_DB_CREATE_EXISTS:
                cursor.execute("DROP DATABASE {} ".format(sql['database_name']))
                cursor.execute("CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(self._db['database_name']))
            else:
                print(err.msg)
        finally:
            cursor.close()
            conn.close()

    def create_table(self):
        try:
            conn = DatabaseConnectionPool.get_instance().get_connection()
            cursor = conn.cursor()
            cursor.execute("USE {}".format(self._db['database_name']))
            for table_name, table_sql in self._db['sql'].items():
                try:
                    print("Creating table {}: ".format(table_name), end='')
                    cursor.execute(table_sql)
                except mysql.connector.Error as err:
                    if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                        print("already exists.")
                    else:
                        print(err.msg)
                else:
                    print("OK")
        except mysql.connector.Error as err:
            print(err)
        finally:
            cursor.close()
            conn.close()

    def create_user(self):
        try:
            conn = DatabaseConnectionPool.get_instance().get_connection()
            cursor = conn.cursor()
            print("Creating user: ", end='')
            cursor.execute(self._db['user_sql'])
            print("OK")
        except mysql.connector.Error as err:
            print(err)
        finally:
            cursor.close()
            conn.close()


if __name__ == "__main__":
    db = DbInit()
    db.create_database()
    db.create_table()
    db.create_user()
