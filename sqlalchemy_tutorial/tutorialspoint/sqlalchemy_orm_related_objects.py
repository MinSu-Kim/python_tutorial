from sqlalchemy import create_engine, func
from sqlalchemy.orm import scoped_session, sessionmaker, relationship

from sqlalchemy_tutorial.tutorialspoint.sqlalchemy_orm_building_relationship import Customer, Invoice, drop_create_table


def insert_data():
    c1 = Customer(name="Gopal Krishna", address="Bank Street Hydarebad", email="gk@gmail.com")
    c1.invoices = [Invoice(invno=10, amount=15000), Invoice(invno=14, amount=3850)]

    c2 = Customer(
            name="Govind Pant",
            address="Gulmandi Aurangabad",
            email="gpant@gmail.com",
            invoices=[Invoice(invno=3, amount=10000), Invoice(invno=4, amount=5000)]
        )

    session.add(c1)
    session.add(c2)
    session.commit()


def insert_all():
    rows = [
        Customer(
            name="Govind Kala",
            address="Gulmandi Aurangabad",
            email="kala@gmail.com",
            invoices=[Invoice(invno=7, amount=12000), Invoice(invno=8, amount=18500)])
        ,
        Customer(
            name="Abdul Rahman",
            address="Rohtak",
            email="abdulr@gmail.com",
            invoices=[Invoice(invno=9, amount=15000), Invoice(invno=11, amount=6000) ])
    ]
    session.add_all(rows)
    session.commit()


if __name__ == "__main__":
    engine = create_engine('mysql+mysqlconnector://user_coffee:rootroot@localhost/coffee?use_pure=True', echo=True)
    session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

    drop_create_table(engine)

    # Customer.invoices = relationship("Invoice", order_by=Invoice.id, back_populates="customer")
    insert_data()

    insert_all()

    for c, i in session.query(Customer, Invoice).filter(Customer.id == Invoice.custid).all():
        print("ID: {} Name: {} Invoice No: {} Amount: {}".format(c.id, c.name, i.invno, i.amount))

    result = session.query(Customer).join(Invoice).filter(Invoice.amount == 18500)
    [print(row.id, row.name, inv.invno, inv.amount) for row in result for inv in row.invoices]

    result = session.query(Customer).outerjoin(Customer.invoices)
    [print(row) for row in result]

    stmt = session.query(Invoice.custid, func.count('*').label('invoice_count')).group_by(Invoice.custid).subquery()
    for u, count in session.query(Customer, stmt.c.invoice_count).\
            outerjoin(stmt, Customer.id == stmt.c.custid).order_by(Customer.id):
        print(u.name, count)