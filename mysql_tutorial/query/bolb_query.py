from mysql.connector import Error

from mysql_tutorial.connect.third_connection_pool.connection_pool import DatabaseConnectionPool


def read_file(filename):
    with open(filename, 'rb') as f:
        photo = f.read()
    return photo


def write_file(data, filename):
    with open(filename, 'wb') as f:
        f.write(data)


def insert_blob(query, filename):
    data = read_file(filename)
    try:
        conn = DatabaseConnectionPool.get_instance().get_connection()
        cursor = conn.cursor()
        cursor.execute(query, (data,))
        conn.commit()
    except Error as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


def update_blob(query, filename, no):
    data = read_file(filename)
    args = (data, no)
    try:
        conn = DatabaseConnectionPool.get_instance().get_connection()
        cursor = conn.cursor()
        cursor.execute(query, args)
        conn.commit()
    except Error as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


def read_blob(query, no, filename):
    try:
        conn = DatabaseConnectionPool.get_instance().get_connection()
        cursor = conn.cursor()
        cursor.execute(query, (no,))
        photo = cursor.fetchone()[0]
        write_file(photo, filename)
    except Error as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


def delete_blob(sql, no):
    try:
        conn = DatabaseConnectionPool.get_instance().get_connection()
        cursor = conn.cursor()
        cursor.execute(sql, (no,))
        conn.commit()
    except Error as error:
        print(error)
    finally:
        cursor.close()
        conn.close()


if __name__ == "__main__":
    data = read_file('../../data/web.png')
    print(type(data))

    update_query = "UPDATE images SET pic=%s WHERE no=%s"
    insert_query = "INSERT INTO images (pic) VALUES(%s)"
    select_query = "SELECT pic FROM images WHERE no = %s"
    delete_query = "delete from images where no = %s"

    insert_blob(insert_query, '../../data/web.png')
    read_blob(select_query, 1, "web.png")
    update_blob(update_query, '../../data/saveFigTest3.png', 1)
    read_blob(select_query, 1, "load.png")
    delete_blob(delete_query, 1)