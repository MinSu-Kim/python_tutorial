import sqlalchemy
from sqlalchemy import String, bindparam, create_engine

from sqlalchemy_tutorial.tutorialspoint.sqlalchemy_core_create_table import students


def insert_students(engine):
    global conn, ins, result
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


if __name__ == "__main__":
    print(sqlalchemy.__version__)
    engine = create_engine('mysql+mysqlconnector://user_coffee:rootroot@localhost/coffee?use_pure=True', echo=True)
    #
    # Base.metadata.drop_all(bind=engine, tables=[Student.__table__])
    # students.drop(bind=engine)
    # # create_all()함수는 엔진 개체를 사용하여 모든 정의된 테이블 개체를 생성하고 정보를 메타 데이터에 저장
    # Base.metadata.create_all(engine)
    # meta.create_all(engine)

    # CRUD 작업
    ins = students.insert()
    print(str(ins))

    ins = students.insert().values(name='minsu', lastname='kim')
    print(str(ins), ins.compile().params, sep='\n')

    insert_students()

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

    # SQLAlchemy에서 Alias ​​구문을 생성하는 From Clause.alias () 메서드를 사용하여 Table, select () 구문 또는 기타 선택 가능한 개체를 별칭으로 바꿀 수 있습니다 .
    # sqlalchemy.sql 모듈의 alias () 함수는 일반적으로 AS 키워드를 사용하여 SQL 문 내의 모든 테이블 또는 부속 선택에 적용되는 별명을 나타냅니다.
    st = students.alias("a")
    s = select([st]).where(st.c.id > 2)
    print(s)
    result = conn.execute(s).fetchall()
    [print(row) for row in result]

    result = conn.execute(s).fetchone()
    print(result)


