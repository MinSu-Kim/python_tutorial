from sqlalchemy import create_engine, ForeignKey, Column, Integer, String

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, scoped_session, sessionmaker

Base = declarative_base()


class Invoice(Base):
    __tablename__ = 'invoices'
    id = Column(Integer, primary_key=True)
    custid = Column(Integer, ForeignKey('customers.id'))
    invno = Column(Integer)
    amount = Column(Integer)
    customer = relationship("Customer", back_populates="invoices")

    def __repr__(self):
        return "<Invoice(id='{0}', custid='{1}', invno='{2}', amount='{3}', customer='{4}'>".\
            format(self.id, self.custid, self.invno, self.amount, self.customer)


class Customer(Base):
    __tablename__ = 'customers'
    id = Column(Integer, primary_key=True)
    name = Column(String(length=20))
    address = Column(String(length=60))
    email = Column(String(length=60))
    invoices = relationship(  # 자식 클래스부터 정의한후 나열
        "Invoice",
        order_by=Invoice.id,
        back_populates="customer")

    def __repr__(self):
        return "<Customers(id='{0}', name='{1}', address='{2}', email='{3}'>".format(self.id, self.name, self.address,
                                                                                     self.email)

def drop_create_table(engine):
    Base.metadata.drop_all(bind=engine, tables=[Invoice.__table__, Customer.__table__])
    Base.metadata.create_all(engine)


if __name__ == "__main__":
    engine = create_engine('mysql+mysqlconnector://user_coffee:rootroot@localhost/coffee?use_pure=True', echo=True)
    session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

    # Base.metadata.drop_all(bind=engine, tables=[Invoice.__tablename__, Customers.__table__])

    Customer.invoices = relationship("Invoice", order_by=Invoice.id, back_populates="customer")
    Base.metadata.create_all(engine)

