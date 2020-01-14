import pandas as pd
from mysql.connector import Error

from mysql_tutorial.coffee_sale.connection_pool import DatabaseConnectionPool
from mysql_tutorial.query.fetch_query import query_with_fetchall2


def delete_product(sql, code):
    try:
        conn = DatabaseConnectionPool.get_instance().get_connection()
        cursor = conn.cursor()
        cursor.execute(sql, (code,))
        conn.commit()
    except Error as error:
        print(error)
    finally:
        cursor.close()
        conn.close()


if __name__ == "__main__":
    res = query_with_fetchall2("select code, name from product where code like 'C___'")
    columns_list = ['code', 'name']
    df = pd.DataFrame(res, columns=columns_list)
    print(df)

    delete_sql = "delete from product where code = %s"
    delete_product(delete_sql, 'C004')

    for code, name in (query_with_fetchall2("select code, name from product where code like 'C___'")):
        print(code , " ", name)