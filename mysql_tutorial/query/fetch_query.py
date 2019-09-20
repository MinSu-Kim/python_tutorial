from mysql.connector import Error
from mysql_tutorial.connect.third_connection_pool.connection_pool import DatabaseConnectionPool


def query_with_fetchone(sql):
    try:
        conn = DatabaseConnectionPool.get_instance().get_connection()
        cursor = conn.cursor()
        cursor.execute(sql)
        row = cursor.fetchone()
        while row is not None:
            print(type(row), " : ", row)
            row = cursor.fetchone()
    except Error as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


def query_with_fetchall(sql):
    try:
        conn = DatabaseConnectionPool.get_instance().get_connection()
        cursor = conn.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        print('Total Row(s):', cursor.rowcount)
        for row in rows:
            print(type(row), " ", row)
    except Error as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


def query_with_fetchall2(sql):
    try:
        conn = DatabaseConnectionPool.get_instance().get_connection()
        cursor = conn.cursor()
        cursor.execute(sql)
        return cursor.fetchall()
    except Error as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


def iter_row(cursor, size=5):
    while True:
        rows = cursor.fetchmany(size)
        if not rows:
            break
        for row in rows:
            yield row


def query_with_fetchmany(sql):
    try:
        conn = DatabaseConnectionPool.get_instance().get_connection()
        cursor = conn.cursor()
        cursor.execute(sql)
        for row in iter_row(cursor, 10):
            print(type(row), " ", row)
    except Error as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


if __name__ == '__main__':
    sql = "select * from product"
    res = query_with_fetchall2(sql)
    print(type(res), 'size = ',  len(res))
    for pno, pname in res:
        print(pno, pname)
    # query_with_fetchone(sql)
    # query_with_fetchmany(sql)

    # dao = ProductDao()
    # pdt = Product('C001', '라떼')
    # dao.insert_product(pdt)

    # query_with_fetchmany(sql)
