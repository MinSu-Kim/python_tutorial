from mysql.connector import Error
from mysql_tutorial.coffee_sale.connection_pool import DatabaseConnectionPool
from mysql_tutorial.query.fetch_query import query_with_fetchall


def insert_product(sql, code, name):
    args = (code, name)
    try:
        conn = DatabaseConnectionPool.get_instance().get_connection()
        cursor = conn.cursor()
        cursor.execute(sql, args)
        conn.commit()
    except Error as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


def insert_products(sql, products):
    try:
        conn = DatabaseConnectionPool.get_instance().get_connection()
        cursor = conn.cursor()
        cursor.executemany(sql, products)
        conn.commit()
    except Error as e:
        print('Error:', e)
    finally:
        cursor.close()
        conn.close()


if __name__ == '__main__':
    select_sql = "select * from product"
    insert_sql = "Insert into product values(%s, %s)"

    products = [('C002', '라떼2'), ('C003', '라떼3'), ('C004', '라떼4')]

    insert_products(insert_sql, products)
    query_with_fetchall(select_sql)