import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, text, ForeignKey

print(sqlalchemy.__version__)
engine = sqlalchemy.create_engine('mysql+mysqlconnector://user_coffee:rootroot@localhost/coffee?use_pure=True', echo=True)

# Define and create the table
# 테이블을 정의
"""
    ORM에서는 처음에 데이터베이스 테이블을 써먹을 수 있게 설정한 다음 직접 정의한 클래스에 맵핑을 해야한다. 
    sqlalchemy에서는 두가지가 동시에 이뤄지는데 Declarative 란걸 이용해 클래스를 생성하고 실제 디비 테이블에 연결을 한다.
"""
Base = declarative_base()


class Product(Base):
    __tablename__ = 'product'
    code = Column(String(length=4), primary_key=True)
    name = Column(String(length=20))

    def __repr__(self):
        return "<Product(code='{0}', name='{1}'>".format(self.code, self.name)


class Sale(Base):
    __tablename__ = 'sale'
    no = Column(Integer, primary_key=True)
    code = Column(String(length=4), ForeignKey(''))
    price = Column(Integer)
    saleCnt = Column(Integer)
    marginRate = Column(Integer)

    def __repr__(self) -> str:
        return "<Sale(no={}, code={}, price={}, saleCnt={}, marginRate={}>".format(
            self.no, self.code, self.price, self.saleCnt, self.marginRate)


class SaleDetail(Base):
    __tablename__ = 'sale_detail'
    no = Column(Integer, primary_key=True)
    sale_price = Column(Integer)
    addTax = Column(Integer)
    supply_price = Column(Integer)
    margin_price = Column(Integer)

    def __repr__(self) -> str:
        return "<SaleDetail(no={}, sale_price={}, addTax={}, supply_price={}, margin_price={}>".format(
            self.no, self.sale_price, self.addTax, self.supply_price, self.margin_price)


print("Product.__table__ =", Product.__table__,"\nProduct.__mapper__ =", Product.__mapper__)
print("Sale.__table__ =", Sale.__table__,"\nSale.__mapper__ =", Sale.__mapper__)
print("SaleDetail.__table__ =", SaleDetail.__table__,"\nSaleDetail.__mapper__ =", SaleDetail.__mapper__)

Base.metadata.create_all(engine)

# Create a session
Session = sqlalchemy.orm.sessionmaker()
Session.configure(bind=engine)
session = Session()

