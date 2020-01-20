import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from sqlalchemy.ext.declarative import declarative_base
# from ConnectingValue import password, id, host, db

print(sqlalchemy.__version__)

re_str = 'mysql+mysqlconnector://user_coffee:rootroot@localhost/coffee?use_pure=True'
engine = sqlalchemy.create_engine(re_str, echo=True)

"""
convert_unicode를 True로 설정하면 String 기반의 모든 column 값을 python unicode object를 수용할 수 있는 값으로 변환
poolsize의 경우 연결할 수 있는 connection의 크기를 지정하고, pool_recycle의 경우 주어진 초 이후에 connection을 재사용하겠다는 뜻
-> 500초 이후에 해당 connection을 재사용하겠다는 뜻

mysql의 경우 일정 시간동안 connection이 없을 경우 connection을 끊어버리게 되는데 pool_recycle을 설정함으로써 강제로 끊어지는 현상을 막을 수가 있다
참고로 pool_recycle 시간이 mysql의 wait_timeout 시간보다 작게 설정되어야 한다. (더 크게 설정이 된다면 mysql에서 이미 connection을 끊었기 때문에 의미가 없다.) -1로 설정할 경우에는 따로 timeout을 두지 않겠다는 뜻이다.
max_overflow는 허용된 connection 수 이상이 들어왔을 때, 최대 얼마까지는 허용
"""
engine = create_engine(re_str, convert_unicode=False, pool_size=20, pool_recycle=500, max_overflow=20)

"""
sessionmaker는 sqlalchemy에서 제공하는 class로 session을 만들어 주는 factory라고 생각하면 될 것 같다. 
일반적으로 sessionmaker를 db 엔진과 연결한 후 session을 생성
session 생성 시 scoped_session을 이용하는데, 이는 session의 범위를 쓰레드 단위로 생성해 준다고 생각하면 된다.
"""
session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
print("scoped_session을 사용하지 않았을 때의 session 값")
for i in range(5):
    print(session())

print()

session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
print("scoped_session을 사용할 때의 session 값")
for i in range(5):
    print(session())
