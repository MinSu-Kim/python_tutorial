"""
SQLAlchemy의 Object Relational Mapper API의 주요 목표
 사용자 정의 Python 클래스를 데이터베이스 테이블과 연관시키고 해당 클래스의 오브젝트를 해당 테이블의 행과 연관시키는 것을 용이하게하는 것

 기본 클래스는 선언 시스템에 클래스 및 맵핑 된 테이블의 catlog를 저장합니다. 이것을 선언적 기본 클래스라고합니다.
 일반적으로 가져온 모듈에는 일반적으로이베이스의 인스턴스가 하나만 있습니다.

 declarative_base() 함수는 기본 클래스를 만드는 데 사용.
    이 함수는 sqlalchemy.ext.declarative 모듈에 정의.
"""
from sqlalchemy import create_engine, Column, Integer, String, update, and_, or_
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.orm.exc import MultipleResultsFound

Base = declarative_base()

"""
다음 코드는 고객의 클래스를 정의합니다. 맵핑 할 테이블과 테이블의 열 이름 및 데이터 유형을 포함.

Declarative의 클래스에는 __tablename__ 특성과 기본 키의 일부인 하나 이상의 Column 이 있어야 합니다. 
Declarative는 모든 Column 객체를 descriptors 라고하는 특별한 Python 접근 자로 바꿉니다 . 
이 프로세스는 SQL 컨텍스트에서 테이블을 참조하는 수단을 제공하고 데이터베이스에서 열 값을 유지하고로드 할 수있는 수단으로 알려져 있습니다.

일반 Python 클래스와 같은 이 맵핑 된 클래스에는 요구 사항에 따라 속성 및 메소드가 있습니다.
선언적 시스템의 클래스에 대한 정보를 테이블 메타 데이터라고합니다. 
SQLAlchemy는 Table 개체를 사용하여 Declarative가 만든 특정 테이블에 대한이 정보를 나타냅니다. 
Table 개체는 사양에 따라 만들어지며 Mapper 개체를 구성하여 클래스와 연결됩니다. 
이 매퍼 객체는 직접 사용되지 않지만 내부적으로 매핑 된 클래스와 테이블 간의 인터페이스로 사용됩니다.
각 Table 객체는 MetaData로 알려진 더 큰 컬렉션의 멤버 이며이 객체는 선언적 기본 클래스의 .metadata 속성을 사용하여 사용할 수 있습니다 .
MetaData.create_all() 메소드는 데이터베이스 연결의 근원으로 우리의 엔진에 전달합니다. 
아직 작성되지 않은 모든 테이블에 대해 데이터베이스에 CREATE TABLE 문을 발행합니다.
"""


class Customers(Base):
    __tablename__ = 'customers'
    id = Column(Integer, primary_key=True)
    name = Column(String(length=20))
    address = Column(String(length=60))
    email = Column(String(length=60))

    def __repr__(self):
        return "<Customers(id='{0}', name='{1}', address='{2}', email='{3}'>".format(self.id, self.name, self.address, self.email)


if __name__ == "__main__":
    engine = create_engine('mysql+mysqlconnector://user_coffee:rootroot@localhost/coffee?use_pure=True', echo=True)
    session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

    Base.metadata.drop_all(bind=engine, tables=[Customers.__table__])
    Base.metadata.create_all(engine)

    """
    Creating Session
    데이터베이스와 상호 작용하려면 핸들을 가져와야합니다. 
    세션 객체는 데이터베이스에 대한 핸들입니다. 
    세션 클래스는 sessionmaker ()를 사용하여 정의됩니다. 
    구성 가능한 세션 팩토리 메소드는 이전에 생성 된 엔진 객체에 바인딩됩니다.
    
    세션 클래스에서 자주 필요한 몇 가지 메소드
        begin() - begins a transaction on this session
        add() - places an object in the session. Its state is persisted in the database on next flush operation
        add_all() - adds a collection of objects to the session
        commit() - flushes all items and any transaction in progress
        delete() - marks a transaction as deleted
        execute() - executes a SQL expression
        expire() - marks attributes of an instance as out of date
        flush() - flushes all object changes to the database
        invalidate() - closes the session using connection invalidation
        rollback() - rolls back the current transaction in progress
        close() - Closes current session by clearing all items and ending any transaction in progress
    """


    #  테이블에 객체를 추가하는 방법
    c1 = Customers(name='Ravi Kumar', address='Station Road Nanded', email='ravi@gmail.com')
    session.add(c1)
    session.commit()

    session.add_all([
        Customers(name='Komal Pande', address='Koti, Hyderabad', email='komal@gmail.com'),
        Customers(name='Rajender Nath', address='Sector 40, Gurgaon', email='nath@gmail.com'),
        Customers(name='S.M.Krishna', address='Budhwar Peth, Pune', email='smk@gmail.com')]
    )
    session.commit()

    res = session.query(Customers).all()
    [print(customer) for customer in res]

    customer_by_id_two = session.query(Customers).get(2)
    print(customer_by_id_two)

    customer_by_id_two.address = 'Banjara Hills Secunderabad'
    session.commit()

    print(session.query(Customers).get(2))

    x = session.query(Customers).first()
    print(x)

    x.name = 'Ravi Shrivastava'
    print(x)

    x = session.query(Customers).first()
    print(x)

    session.rollback()

    x = session.query(Customers).first()
    print(x)

    """
    대량 업데이트의 경우 Query 객체의 update () 메서드를 사용해야합니다. 
    접두사 'Mr'을 시도해 봅시다. 각 행에서 이름을 지정할 수 있습니다 (ID = 2 제외). 해당 update () 문은 다음과 같습니다-
    """
    res = session.query(Customers).all()
    [print(customer) for customer in res]

    """
    update () 메소드에는 다음과 같은 두 개의 매개 변수가 필요합니다.
        키가 업데이트 될 속성이고 값이 속성의 새로운 내용 인 키-값 사전.
        세션에서 속성을 업데이트하는 전략을 언급하는 synchronize_session 속성. 유효한 값은 false입니다. 
        세션을 동기화하지 않으려면 가져 오기 : 업데이트 전에 선택 쿼리를 수행하여 업데이트 쿼리와 일치하는 개체를 찾습니다. 평가 : 세션의 객체에 대한 기준을 평가합니다.
    """
    session.query(Customers).filter(Customers.id != 2).update({Customers.name: "Mr." + Customers.name}, synchronize_session=False)
    session.commit()

    res = session.query(Customers).all()
    [print(customer) for customer in res]

    result = session.query(Customers).filter(Customers.id > 2)
    [print(customer) for customer in result]

    result = session.query(Customers).filter(Customers.id == 2)
    [print(customer) for customer in result]

    result = session.query(Customers).filter(Customers.id != 2)
    [print(customer) for customer in result]

    result = session.query(Customers).filter(Customers.name.like('%Ra%'))
    [print(customer) for customer in result]

    result = session.query(Customers).filter(Customers.id.in_([1, 3]))
    [print(customer) for customer in result]

    result = session.query(Customers).filter(Customers.id > 2, Customers.name.like('%Ra%'))
    [print(customer) for customer in result]

    result = session.query(Customers).filter(and_(Customers.id > 2, Customers.name.like('%Ra%')))
    [print(customer) for customer in result]

    result = session.query(Customers).filter(or_(Customers.id > 2, Customers.name.like('%Ra%')))
    [print(customer) for customer in result]

    """
    all() - It returns a list. Given below is the line of code for all() function.
    """
    [print(customer) for customer in session.query(Customers).all()]

    """
    first() - It applies a limit of one and returns the first result as a scalar.
    """
    print(session.query(Customers).first())

    """
    one() - 이 명령은 모든 행을 완전히 페치하며 결과에 정확히 하나의 오브젝트 ID 또는 복합 행이 없으면 오류가 발생합니다.
    MultipleResultsFound: Multiple rows were found for one()
    """
    try:
        res = session.query(Customers).one()
        print(res)
    except MultipleResultsFound:
        print("결과에 정확히 하나의 오브젝트 ID 또는 복합 행이 없으면 오류가 발생")



    """
    scalar() - 그것은 one () 메소드를 호출하고 성공하면 다음과 같이 행의 첫 번째 열을 반환합니다-
    """
    print(session.query(Customers).filter(Customers.id == 3).scalar())

    from sqlalchemy import text
    [print(cust) for cust in session.query(Customers).filter(text("id<3"))]

    cust = session.query(Customers).filter(text("id = :value")).params(value=1).one()
    print(cust)

    """
    session.query(Customers).from_statement(text("SELECT * FROM customers")).all()
    위 코드의 결과는 아래와 같이 기본 SELECT 문이됩니다.
    SELECT * FROM customers
    """
    [print(cust) for cust in session.query(Customers).from_statement(text("SELECT * FROM customers")).all()]
    [print(cust) for cust in session.query(Customers).all()]

    stmt = text("SELECT id, name, address, email FROM customers")
    stmt = stmt.columns(Customers.id, Customers.name)
    [print(cust) for cust in session.query(Customers.id, Customers.name).from_statement(stmt).all()]
    print()
    [print(cust) for cust in session.query(Customers.id, Customers.name).all()]