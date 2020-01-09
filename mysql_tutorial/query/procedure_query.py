from mysql.connector import MySQLConnection, Error

from mysql_tutorial.connect.third_connection_pool.connection_pool import DatabaseConnectionPool


def call_sale_stat_sp(query):
    try:
        conn = DatabaseConnectionPool.get_instance().get_connection()
        cursor = conn.cursor()
        cursor.callproc(query)
        for result in cursor.stored_results():
            res = result.fetchone()
            print(res)
    except Error as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

# call_sale_stat_sp('proc_sale_stat')


def call_order_price_by_issale(query, isSale):
    try:
        conn = DatabaseConnectionPool.get_instance().get_connection()
        cursor = conn.cursor()

        args = [isSale,]
        cursor.callproc(query, args)
        for result in cursor.stored_results():
            rows = result.fetchall()
            for row in rows:
                print(row)
    except Error as e:
        print(e)
    finally:
        cursor.close()
        conn.close()



call_order_price_by_issale('proc_order_price', False)
print()
call_order_price_by_issale('proc_order_price', True)