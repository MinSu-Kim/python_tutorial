import sqlalchemy
from sqlalchemy import Table, Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class Association(Base):
    __tablename__ = 'association'
    left_id = Column(Integer, ForeignKey('left.id'), primary_key=True)
    right_id = Column(Integer, ForeignKey('right.id'), primary_key=True)
    extra_data = Column(String(50))
    child = relationship("Right")


class Left(Base):
    __tablename__ = 'left'
    id = Column(Integer, primary_key=True)
    children = relationship("Association")


class Right(Base):
    __tablename__ = 'right'
    id = Column(Integer, primary_key=True)


if __name__ == "__main__":
    print(sqlalchemy.__version__)
    engine = sqlalchemy.create_engine('mysql+mysqlconnector://user_coffee:rootroot@localhost/coffee?use_pure=True', echo=True)


    Base.metadata.drop_all(bind=engine, tables=[Association.__table__])
    Base.metadata.drop_all(bind=engine, tables=[Right.__table__])
    Base.metadata.drop_all(bind=engine, tables=[Left.__table__])

    # Base.metadata.create_all(engine)