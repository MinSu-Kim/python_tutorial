from mysql.connector import Error

from mysql_tutorial.connect.third_connection_pool.connection_pool2 import get_implicitly_connection, \
    ExplicitlyConnectionPool


def transaction_test1():
    try:
        print('Connecting to MySQL database...')
        conn = get_implicitly_connection()
        print(type(conn))
        conn.autocommit = False
        cursor = conn.cursor()
        insert_sql = "Insert into product values(%s, %s)"
        cursor.execute(insert_sql, ('D001', ' 아메리카노'))  # 이미 존재하므로 예외발생
        cursor.execute(insert_sql, ('C005', '라떼5'))
        print("Record 2 product successfully ")
        conn.commit()
    except Error as error:
        print("Failed to update record to database rollback: {}".format(error))
        conn.rollback()
    finally:
        if conn.is_connected():
            conn.autocommit = True
            cursor.close()
            conn.close()
            print("connection is closed")


def transaction_test2():
    try:
        print('Connecting to MySQL database...')
        conn = ExplicitlyConnectionPool.get_instance().get_connection()
        print(type(conn))
        conn.autocommit = False
        cursor = conn.cursor()
        insert_sql = "Insert into product values(%s, %s)"
        cursor.execute(insert_sql, ('D001', ' 아메리카노'))  # 이미 존재하므로 예외발생
        cursor.execute(insert_sql, ('C005', '라떼5'))
        print("Record 2 product successfully ")
        conn.commit()
    except Error as error:
        print("Failed to update record to database rollback: {}".format(error))
        conn.rollback()
    finally:
        if conn.is_connected():
            conn.autocommit = True
            cursor.close()
            conn.close()
            print("connection is closed")


if __name__ == "__main__":
    transaction_test1()
    transaction_test2()