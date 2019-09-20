from mysql.connector import Error

from mysql_tutorial.coffee_sale.connection_pool import DatabaseConnectionPool


def update_product(sql, name, code):
    args = (name, code)
    try:
        conn = DatabaseConnectionPool.get_instance().get_connection()
        cursor = conn.cursor()
        cursor.execute(sql, args)
        conn.commit()
    except Error as error:
        print(error)
    finally:
        cursor.close()
        conn.close()


def select_product_by_code(sql):
    try:
        conn = DatabaseConnectionPool.get_instance().get_connection()
        cursor = conn.cursor()
        cursor.execute(sql)
        return cursor.fetchone()
    except Error as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


if __name__ == "__main__":
    select_sql = "select code, name from product where code = '{code}'".format(code='C001')
    res = select_product_by_code(select_sql)
    print(res)

    update_sql = "update product set name = %s where code = %s"
    update_product(update_sql, '라떼수정', 'C001')

    print(select_product_by_code(select_sql))