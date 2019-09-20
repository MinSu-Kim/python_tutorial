from mysql_tutorial.connect.third_connection_pool.connection_pool2 \
    import ExplicitlyConnectionPool, get_implicitly_connection

if __name__ == '__main__':
    print("Explicitly ConnectionPool")
    connection = ExplicitlyConnectionPool.get_instance().get_connection()
    print(type(connection), connection)

    cursor = connection.cursor()
    cursor.execute("select * from product where code like 'C___'")
    rows = cursor.fetchall()

    print('Total Row(s):', cursor.rowcount)
    for row in rows:
        print(type(row), " => ", row)
    connection.close()

    print("Implicitly ConnectionPool")
    connection = get_implicitly_connection()
    print(type(connection), connection)
    cursor = connection.cursor()
    cursor.execute("select * from product where code like 'C___'")
    rows = cursor.fetchall()

    print('Total Row(s):', cursor.rowcount)
    for row in rows:
        print(type(row), " => ", row)
    connection.close()
