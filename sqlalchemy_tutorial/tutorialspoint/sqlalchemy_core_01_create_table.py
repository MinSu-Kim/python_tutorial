"""
SQL 표현식 언어는 테이블 열에 대해 표현식을 구성
SQLAlchemy Column 오브젝트는 데이터베이스 테이블의 컬럼을 나타내며, 이는 Tableobject 로 표시.
메타 데이터에는 테이블, 인덱스, 뷰, 트리거 등과 같은 관련 개체에 대한 정의가 포함

SQLAlchemy Metadata의 MetaData 클래스 개체는 Table 개체와 관련 스키마 구성의 모음
"""
import sqlalchemy
from sqlalchemy import Table, Column, Integer, String, MetaData, String, bindparam
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

meta = MetaData()

students = Table(
    'students',
    meta,
    Column('id', Integer, primary_key=True),
    Column('name', String(length=20)),
    Column('lastname', String(length=30)),
)

"""
    ORM에서는 처음에 데이터베이스 테이블을 써먹을 수 있게 설정한 다음 직접 정의한 클래스에 맵핑을 해야한다. 
    sqlalchemy에서는 두가지가 동시에 이뤄지는데 Declarative 란걸 이용해 클래스를 생성하고 실제 디비 테이블에 연결을 한다.
"""
Base = declarative_base()


class Student(Base):
    __tablename__ = 'student'
    no = Column(Integer, primary_key=True)
    name = Column(String(length=20))
    kor = Column(Integer)
    end = Column(Integer)
    math = Column(Integer)


if __name__ == "__main__":
    print(sqlalchemy.__version__)
    engine = create_engine('mysql+mysqlconnector://user_coffee:rootroot@localhost/coffee?use_pure=True', echo=True)

    Base.metadata.drop_all(bind=engine, tables=[Student.__table__])
    students.drop(bind=engine)
    # create_all()함수는 엔진 개체를 사용하여 모든 정의된 테이블 개체를 생성하고 정보를 메타 데이터에 저장
    Base.metadata.create_all(engine)
    meta.create_all(engine)

    # CRUD 작업
    ins = students.insert()
    print(str(ins))

    ins = students.insert().values(name='minsu', lastname='kim')
    print(str(ins), ins.compile().params, sep='\n')

    conn = engine.connect()
    ins = students.insert().values(name='Ravi', lastname='Kapoor')
    print(str(ins), ins.compile().params, sep='\n')
    # 결과 변수를 ResultProxy 객체 라고 합니다 . DBAPI 커서 객체와 유사
    result = conn.execute(ins)

    print(str(ins), ins.compile().params, type(result), result, sep='\n')

    # ResultProxy.inserted_primary_key 를 사용하여 명령문에서 생성 된 기본 키 값에 대한 정보
    print("result.inserted_primary_key = ", result.inserted_primary_key)

    conn.execute(students.insert(), [
        {'name': 'Rajiv', 'lastname': 'Khanna'},
        {'name': 'Komal', 'lastname': 'Bhandari'},
        {'name': 'Abdul', 'lastname': 'Sattar'},
        {'name': 'Priya', 'lastname': 'Rajhans'},
    ])

    # 테이블 객체의 select () 메소드를 사용하 SELECT 표현식을 생성여
    s = students.select()
    print(s)
    result = conn.execute(s)
    print(type(result), result)

    # 결과 변수는 DBAPI의 커서와 같습니다. 이제 fetchone () 메소드를 사용하여 레코드를 가져올 수 있습니다 .
    [print(row) for row in result]

    # SELECT 쿼리의 WHERE 절은 Select.where () 를 사용하여 적용 c 속성은 열의 별명
    s = students.select().where(students.c.id > 2)
    result = conn.execute(s)
    [print(row) for row in result]

    from sqlalchemy.sql import select
    s = select([students])
    result = conn.execute(s)
    [print(row) for row in result]

    s = select([students]).where(students.c.id > 2)
    result = conn.execute(s)
    [print(row) for row in result]

    from sqlalchemy import text
    t = text("SELECT * FROM students")
    result = conn.execute(t)
    [print(row) for row in result]

    from sqlalchemy.sql import text
    s = text("select students.name, students.lastname from students where students.name between :x and :y")
    result = conn.execute(s, x='A', y='L').fetchall()
    [print(row) for row in result]

    # text () 구문은 TextClause.bindparams () 메서드를 사용하여 미리 설정된 바운드 값을 지원
    stmt = text("SELECT * FROM students WHERE students.name BETWEEN :x AND :y")

    stmt = stmt.bindparams(
        bindparam("x", type_=String),
        bindparam("y", type_=String)
    )

    result = conn.execute(stmt, {"x": "A", "y": "L"})
    [print(row) for row in result]

    s = select([text("students.name, students.lastname from students")]).where(text("students.name between :x and :y"))
    result = conn.execute(s, x='A', y='L').fetchall()
    [print(row) for row in result]

    # and_ () 함수를 사용하여 text () 함수의 도움으로 작성된 WHERE 절에서 여러 조건을 결합 할 수도 있습니다 .
    from sqlalchemy import and_
    from sqlalchemy.sql import select

    s = select([text("* from students")]) \
        .where(
        and_(
            text("students.name between :x and :y"),
            text("students.id>2")
        )
    )
    result = conn.execute(s, x='A', y='L').fetchall()
    [print(row) for row in result]