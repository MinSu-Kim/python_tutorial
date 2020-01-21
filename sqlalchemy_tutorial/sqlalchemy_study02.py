import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

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
    code = Column(String(length=4))
    price = Column(Integer)
    saleCnt = Column(Integer)
    marginRate = Column(Integer)

    def __repr__(self) -> str:
        return "<Sale(no={}, code={}, price={}, saleCnt={}, marginRate={}>".format(
            self.no, self.code, self.price, self.saleCnt, self.marginRate)


print("Product.__table__ =", Product.__table__,"\nUser.__mapper__ =", Product.__mapper__)

Base.metadata.create_all(engine)

# Create a session
Session = sqlalchemy.orm.sessionmaker()
Session.configure(bind=engine)
session = Session()

"""
insert
new_product = Product(code='C001')
session.add(new_product)
session.commit()
"""

pdt = session.query(Product).filter_by(code='A004').first()
print('\nProduct:')
print(pdt)

pdts = session.query(Product)
print(type(pdts))
[print(p) for p in pdts]

pdt_a = session.query(Product).filter(Product.code.like('A%'))
[print(p) for p in pdt_a]

# equals
[print(p) for p in session.query(Product).filter(Product.code == 'A003')]
# not equals
[print(p) for p in session.query(Product).filter(Product.code != 'A003')]
# in
[print(p) for p in session.query(Product).filter(Product.code.in_(['A001', 'B001']))]
# not in
[print(p) for p in session.query(Product).filter(~Product.code.in_(['A001', 'B001']))]
# like
[print(p) for p in session.query(Product).filter(Product.code.like('%3'))]
# 서브쿼리
[print(p) for p in session.query(Sale).filter(Sale.code.in_(session.query(Product.code).filter(Product.code == 'A001')))]
# is null
[print(p) for p in session.query(Product).filter(Product.name == None)]
# is not null
[print(p) for p in session.query(Product).filter(Product.name != None)]
# and
[print(p) for p in session.query(Product).filter(Product.code == 'A%').filter(Product.name=='헤이즐넛')]
from sqlalchemy import and_
[print(p) for p in session.query(Product).filter(and_(Product.code == 'A001', Product.name == '아메리카노'))]
# or
from sqlalchemy import or_
[print(p) for p in session.query(Product).filter(or_(Product.code == 'A001', Product.code == 'B002'))]

# match
"""
ALTER TABLE 테이블이름
ADD FULLTEXT INDEX이름 (필드이름)
alter table product add fulltext index idx_fulltext (code);
"""
[print(p) for p in session.query(Product).filter(Product.code.match('A003'))]


"""
리스트와 Scalars 반환하기
Query 객체의 all(), one(), first() 메소드는 즉시 SQL을 호출하고 non-iterator 값을 반환한다. all()은 리스트를 반환
first()는 첫째를 리밋으로 설정해 scalar로 가져온다.

one()은 모든 행을 참조해 식별자를 값으로 가지고 있지 않거나 여러 행이 동일한 값을 가지고 있는 경우 에러를 만든다.
"""
query = session.query(Product).filter(Product.code.like('A%')).order_by(Product.code)
query_all = query.all()
print(type(query), type(query_all))
[print(p) for p in query_all]

query_first = query.first()
print(type(query_first), query_first)


print("\none()")
from sqlalchemy.orm.exc import MultipleResultsFound
try:
    product_user = query.one()
    print(product_user)
except MultipleResultsFound as e:
    print(e)


from sqlalchemy.orm.exc import NoResultFound
try:
    product_user = query.filter(Product.code == 'A000').one()
    print(product_user)
except NoResultFound as e:
    print(e)


"""
문자로 된 SQL 사용하기
1. 문자열을 Query와 함께 유연하게 쓸 수 있다. 대부분 메소드는 문자열을 수용한다. 예를 들면 filter()와 order_by()에서 쓸 수 있다.
"""

print("문자로 된 SQL 사용하기")
[print(product) for product in session.query(Product).filter("code = A001").order_by("code").all()]

