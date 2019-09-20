from mysql_tutorial.connect.connection_pool import DatabaseConnectionPool
from mysql_tutorial.dto.Product import Product

class ProductDao:

    def query_with_fetchone(self, _sql):
        conn = DatabaseConnectionPool.get_instance().get_connection()
        cursor = conn.cursor()
        cursor.execute(_sql)
        row = cursor.fetchone()
        while row is not None:
            print(row)
            row = cursor.fetchone()
        cursor.close()
        conn.close()

    def query_with_fetchall(self, _sql):
        conn = DatabaseConnectionPool.get_instance().get_connection()
        cursor = conn.cursor()
        cursor.execute(_sql)
        rows = cursor.fetchall()
        print('Total Row(s):', cursor.rowcount)
        for row in rows:
            print(row)
        cursor.close()
        conn.close()

    def iter_row(self, cursor, size=10):
        while True:
            rows = cursor.fetchmany(size)
            if not rows:
                break
            for row in rows:
                yield row

    def query_with_fetchmany(self, _sql):
        conn = DatabaseConnectionPool.get_instance().get_connection()
        cursor = conn.cursor()

        cursor.execute(_sql)

        for row in self.iter_row(cursor, 10):
            print(row)
        cursor.close()
        conn.close()

    def insert_product(self, product):
        print(str(pdt))

        query = "Insert into product values(%s, %s, %d)"
        args = (product.code, product.name, product.price)
        conn = DatabaseConnectionPool.get_instance().get_connection()
        cursor = conn.cursor()
        cursor.execute(query, args)
        conn.commit()

        cursor.close()
        conn.close()

if __name__ == '__main__':
    dao = ProductDao()
    sql = "select * from product"
    dao.query_with_fetchall(sql)
    # dao.query_with_fetchone(sql)
    # dao.query_with_fetchmany(sql)

    pdt = Product('C001', '라떼', 5000)
    dao.insert_product(pdt)

    dao.query_with_fetchmany(sql)