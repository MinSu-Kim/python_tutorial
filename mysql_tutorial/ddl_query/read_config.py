from configparser import ConfigParser


def read_db_config(filename='sql.ini'):
    parser = ConfigParser()
    parser.read(filename, encoding='UTF8')

    db = {}
    for sec in parser.sections():
        items = parser.items(sec)
        if sec == 'name':
            for key, value in items:
                db[key] = value
        if sec == 'sql':
            sql = {}
            for key, value in items:
                sql[key] = "".join(value.splitlines())
            db['sql'] = sql
        if sec == 'user':
            for key, value in items:
                db[key] = value
    return db


if __name__ == "__main__":
    db = read_db_config()
    print(db)
    for key, value in db.items():
        if key == 'database_name':
            print(value)
        elif key == 'user_sql':
            print(value)
        else:
            for k, v in value.items():
                print(k, "===", v)