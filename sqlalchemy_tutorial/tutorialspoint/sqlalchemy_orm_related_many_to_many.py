from sqlalchemy import create_engine, ForeignKey, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, scoped_session, sessionmaker

Base = declarative_base()


class Department(Base):
    __tablename__ = 'department'
    id = Column(Integer, primary_key=True)
    name = Column(String(length=20))
    employees = relationship('Employee', secondary='link')


class Employee(Base):
    __tablename__ = 'employee'
    id = Column(Integer, primary_key=True)
    name = Column(String(length=20))
    departments = relationship(Department, secondary='link')


class Link(Base):
    __tablename__ = 'link'
    department_id = Column(Integer, ForeignKey('department.id'), primary_key=True)
    employee_id = Column(Integer, ForeignKey('employee.id'), primary_key=True)


if __name__ == "__main__":

    engine = create_engine('mysql+mysqlconnector://user_coffee:rootroot@localhost/coffee?use_pure=True', echo=True, pool_recycle=3600)
    session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

    Base.metadata.drop_all(bind=engine, tables=[Link.__table__, Employee.__table__, Department.__table__])

    Base.metadata.create_all(engine)

    d1 = Department(name="Accounts")
    d2 = Department(name="Sales")
    d3 = Department(name="Marketing")

    e1 = Employee(name="John")
    e2 = Employee(name="Tony")
    e3 = Employee(name="Graham")

    e1.departments.append(d1)
    e2.departments.append(d3)
    d1.employees.append(e3)
    d2.employees.append(e2)
    d3.employees.append(e1)
    e3.departments.append(d2)

    session.add(e1)
    session.add(e2)
    session.add(d1)
    session.add(d2)
    session.add(d3)
    session.add(e3)
    session.commit()

    for x in session.query(Department, Employee).filter(Link.department_id == Department.id,
                                                        Link.employee_id == Employee.id).order_by(
        Link.department_id).all():
        print("Department: {} Name: {}".format(x.Department.name, x.Employee.name))