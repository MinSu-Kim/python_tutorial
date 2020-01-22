import sqlalchemy
from sqlalchemy import String, bindparam, create_engine

from sqlalchemy_tutorial.tutorialspoint.sqlalchemy_core_create_table import students
"""
대상 테이블 오브젝트 의 update() 메소드는 동등한 UPDATE SQL 표현식을 구성

table.update().where(conditions).values(SET expressions)
 - 결과 업데이트 개체의 values​​() 메서드는 UPDATE의 SET 조건을 지정하는 데 사용 
 - None으로두면, SET 조건은 명령문의 실행 및 / 또는 컴파일 중에 명령문에 전달 된 매개 변수에서 결정됩니다.

where 절은 UPDATE 문의 WHERE 조건을 설명하는 선택적 표현식입니다
"""

if __name__ == "__main__":
    print(sqlalchemy.__version__)
    engine = create_engine('mysql+mysqlconnector://user_coffee:rootroot@localhost/coffee?use_pure=True', echo=True)
    con = engine.connect()

    s = students.select()
    [print(row) for row in con.execute(s).fetchall()]

    stmt = students.update().where(students.c.lastname == 'Khanna').values(lastname='Kapoor')
    print(stmt, stmt.compile().params, sep='\n')

    res = con.execute(stmt)
    print(type(res), res)

    s = students.select()
    [print(row) for row in con.execute(s).fetchall()]

    # sqlalchemy.sql.expression 모듈에서 update () 함수를 사용하여 유사한 기능을 수행 할 수도 있습니다.
    from sqlalchemy.sql.expression import update
    stmt = update(students).where(students.c.lastname == 'Sattar').values(lastname='SSSSS')
    con.execute(stmt)

    s = students.select().where(students.c.id == 4)
    print(con.execute(s).fetchone())