from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, ForeignKey, select

meta = MetaData()

students = Table(
   'students', meta,
   Column('id', Integer, primary_key = True),
   Column('name', String(length=20)),
   Column('lastname', String(length=30)),
)

addresses = Table(
   'addresses', meta,
   Column('id', Integer, primary_key = True),
   Column('st_id', Integer, ForeignKey('students.id')),
   Column('postal_add', String(length=60)),
   Column('email_add', String(length=40)))

if __name__ == "__main__":
    engine = create_engine('mysql+mysqlconnector://user_coffee:rootroot@localhost/coffee?use_pure=True', echo=True)

    addresses.drop(bind=engine, checkfirst=True)
    students.drop(bind=engine, checkfirst=True)

    meta.create_all(engine)

    con = engine.connect()
    con.execute(students.insert(), [
        {'name': 'Ravi', 'lastname': 'Kapoor'},
        {'name': 'Rajiv', 'lastname': 'Khanna'},
        {'name': 'Komal', 'lastname': 'Bhandari'},
        {'name': 'Abdul', 'lastname': 'Sattar'},
        {'name': 'Priya', 'lastname': 'Rajhans'},
    ])

    con.execute(addresses.insert(), [
        {'st_id': 1, 'postal_add': 'Shivajinagar Pune', 'email_add': 'ravi@gmail.com'},
        {'st_id': 1, 'postal_add': 'ChurchGate Mumbai', 'email_add': 'kapoor@gmail.com'},
        {'st_id': 3, 'postal_add': 'Jubilee Hills Hyderabad', 'email_add': 'komal@gmail.com'},
        {'st_id': 5, 'postal_add': 'MG Road Bangaluru', 'email_add': 'as@yahoo.com'},
        {'st_id': 2, 'postal_add': 'Cannought Place new Delhi', 'email_add': 'admin@khanna.com'},
    ])

    s = select([students, addresses]).where(students.c.id == addresses.c.st_id)
    print(s)
    result = con.execute(s)
    [print(row) for row in result]