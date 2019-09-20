from mysql_tutorial.coffee_sale.connection_pool import DatabaseConnectionPool


connection = DatabaseConnectionPool.get_instance().get_connection()
cursor = connection.cursor()
cursor.execute("select * from product")
rows = cursor.fetchall()

print('Total Row(s):', cursor.rowcount)
for row in rows:
    print(type(row), " => ",  row)

connection.close()