import sqlalchemy
from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

"""
다대다는 두 클래스 사이에 연관 테이블을 추가합니다. 
연관 테이블은에 relationship() 대한 secondary인수로 표시됩니다 . 
일반적으로 테이블에서는 선언적 기본 클래스와 관련된 MetaData개체를 사용하므로 ForeignKey지침을 통해 연결할 원격 테이블을 찾을 수 있습니다.

association_table = Table('association', Base.metadata,
    Column('left_id', Integer, ForeignKey('left.id')),
    Column('right_id', Integer, ForeignKey('right.id'))
)

class Left(Base):
    __tablename__ = 'left'
    id = Column(Integer, primary_key=True)
    children = relationship("Child", secondary=association_table)

class Right(Base):
    __tablename__ = 'right'
    id = Column(Integer, primary_key=True)

양방향 관계의 경우 관계의 양쪽에 모음이 포함됩니다.
relationship.back_populates를 사용하여 지정하고 각각에 대해 relationship()공통 연관 테이블을 지정하십시오.

association_table = Table('association', Base.metadata,
    Column('left_id', Integer, ForeignKey('left.id')),
    Column('right_id', Integer, ForeignKey('right.id'))
)

class Left(Base):
    __tablename__ = 'left'
    id = Column(Integer, primary_key=True)
    children = relationship(
        "Right",
        secondary=association_table,
        back_populates="parent")


class Right(Base):
    __tablename__ = 'right'
    id = Column(Integer, primary_key=True)
    parents = relationship(
        "Left",
        secondary=association_table,
        back_populates="child")
"""

association_table = Table('association', Base.metadata,
    Column('left_id', Integer, ForeignKey('left.id')),
    Column('right_id', Integer, ForeignKey('right.id'))
)

class Left(Base):
    __tablename__ = 'left'
    id = Column(Integer, primary_key=True)
    children = relationship("Right",
                    secondary=association_table,
                    backref="parents")

class Right(Base):
    __tablename__ = 'right'
    id = Column(Integer, primary_key=True)



if __name__ == "__main__":
    print(sqlalchemy.__version__)
    engine = sqlalchemy.create_engine('mysql+mysqlconnector://user_coffee:rootroot@localhost/coffee?use_pure=True', echo=True)

    # association_table.drop(bind=engine)
    # Base.metadata.drop_all(bind=engine, tables=[Left.__table__])
    # Base.metadata.drop_all(bind=engine, tables=[Right.__table__])

    Base.metadata.create_all(engine)