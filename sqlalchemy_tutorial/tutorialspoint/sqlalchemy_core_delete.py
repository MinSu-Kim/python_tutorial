import sqlalchemy
from sqlalchemy import String, bindparam, create_engine

from sqlalchemy_tutorial.tutorialspoint.sqlalchemy_core_create_table import students, drop_table, create_table
from sqlalchemy_tutorial.tutorialspoint.sqlalchemy_core_select import insert_students

"""
삭제 작업은 다음 명령문에 주어진 대상 테이블 객체에서 delete () 메소드를 실행하여 수행 할 수 있습니다.

stmt = students.delete()
"""

if __name__ == "__main__":
    print(sqlalchemy.__version__)
    engine = create_engine('mysql+mysqlconnector://user_coffee:rootroot@localhost/coffee?use_pure=True', echo=True)

    drop_table(engine)
    create_table(engine)
    insert_students(engine)

    con = engine.connect()
    s = students.select()
    [print(row) for row in con.execute(s).fetchall()]

    stmt = students.delete()
    print(stmt)

    stmt = students.delete().where(students.c.id > 2)
    print(stmt)

    con.execute(stmt)
    s = students.select()
    [print(row) for row in con.execute(s).fetchall()]