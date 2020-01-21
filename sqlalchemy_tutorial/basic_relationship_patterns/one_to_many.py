import sqlalchemy
from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

"""
1. 일대 다 관계는 부모를 참조하는 자식 테이블에 외래 키를 배치
relationship()그런 다음 자식이 나타내는 항목 모음을 참조하여 부모에 지정됩니다.


class Parent(Base):
    __tablename__ = 'parent'
    id = Column(Integer, primary_key=True)
    children = relationship("Child")

class Child(Base):
    __tablename__ = 'child'
    id = Column(Integer, primary_key=True)
    parent_id = Column(Integer, ForeignKey('parent.id'))



print(sqlalchemy.__version__)
engine = sqlalchemy.create_engine('mysql+mysqlconnector://user_coffee:rootroot@localhost/coffee?use_pure=True', echo=True)

Base.metadata.create_all(engine)


일대 다로 양방향 관계를 설정하려면 "역방향"이 다대 일인 경우 추가를 지정 
relationship()하고 relationship.back_populates매개 변수를 사용하여 둘을 연결하십시오 .
Child will get a parent attribute with many-to-one semantics.
Child(다) parent (일) 의미로 속성을 얻습니다 .

class Parent(Base):
    __tablename__ = 'parent'
    id = Column(Integer, primary_key=True)
    children = relationship('Child', back_populates='parent')

class Child(Base):
    __tablename__ = 'child'
    id = Column(Integer, primary_key=True)
    parent_id = Column(Integer, ForeignKey('parent.id'))
    parent = relationship('Parent', back_populates='children')

또는 back_populate를 사용하는 대신 단일 관계()에 backref옵션을 사용할 수 있습니다.
"""
class Parent(Base):
    __tablename__ = 'parent'
    id = Column(Integer, primary_key=True)
    children = relationship('Child', backref='parent')


class Child(Base):
    __tablename__ = 'child'
    id = Column(Integer, primary_key=True)
    parent_id = Column(Integer, ForeignKey('parent.id'))
    parent = relationship('Parent', back_populates='children')

print(sqlalchemy.__version__)
engine = sqlalchemy.create_engine('mysql+mysqlconnector://user_coffee:rootroot@localhost/coffee?use_pure=True', echo=True)

Base.metadata.create_all(engine)