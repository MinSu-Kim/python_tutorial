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


def drop_table(engine):
    Base.metadata.drop_all(bind=engine, tables=[Student.__table__])
    students.drop(bind=engine)
    # create_all()함수는 엔진 개체를 사용하여 모든 정의된 테이블 개체를 생성하고 정보를 메타 데이터에 저장
    create_table(engine)


def create_table(engine):
    Base.metadata.create_all(engine)
    meta.create_all(engine)


if __name__ == "__main__":
    print(sqlalchemy.__version__)
    engine = create_engine('mysql+mysqlconnector://user_coffee:rootroot@localhost/coffee?use_pure=True', echo=True)
    drop_table(engine)
    create_table(engine)