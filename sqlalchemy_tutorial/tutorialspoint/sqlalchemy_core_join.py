"""
oin () 메소드는 한 테이블 오브젝트에서 다른 테이블 오브젝트로 결합 오브젝트를 리턴합니다.

join(right, onclause = None, isouter = False, full = False)
위 코드에서 언급 한 매개 변수의 기능은 다음과 같습니다.
  right -조인의 오른쪽; 이것은 모든 Table 객체
  onclause- 조인의 ON 절을 나타내는 SQL 식 None으로두면 외래 키 관계를 기반으로 두 테이블을 조인하려고 시도합니다.
  isouter -True 인 경우 JOIN 대신 LEFT OUTER JOIN을 렌더링합니다.
  full -True이면 LEFT OUTER JOIN 대신 FULL OUTER JOIN을 렌더링합니다.

예를 들어 join () 메서드를 사용하면 외래 키를 기반으로 자동으로 조인됩니다.
"""
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, ForeignKey, select, and_, or_, asc, \
    desc, between

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


    print(students.join(addresses))

    j = students.join(addresses, students.c.id == addresses.c.st_id)
    stmt = select([students]).select_from(j)



    j = students.join(addresses, students.c.id == addresses.c.st_id)
    stmt = select([students, addresses]).select_from(j)
    result = con.execute(stmt)
    [print(row) for row in result]

    stmt = select([students]).where(and_(students.c.name == 'xyz', students.c.id < 3))
    result = con.execute(stmt)
    [print(row) for row in result.fetchall()]

    stmt = select([students]).where(or_(students.c.name == 'xyz', students.c.id < 3))
    result = con.execute(stmt)
    [print(row) for row in result.fetchall()]

    stmt = select([students]).order_by(asc(students.c.name))
    result = con.execute(stmt)
    [print(row) for row in result.fetchall()]

    stmt = select([students]).order_by(desc(students.c.name))
    result = con.execute(stmt)
    [print(row) for row in result.fetchall()]

    stmt = select([students]).where(between(students.c.id, 2, 4))
    result = con.execute(stmt)
    [print(row) for row in result.fetchall()]