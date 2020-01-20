import sqlalchemy
from sqlalchemy import create_engine

print(sqlalchemy.__version__)
engine = create_engine('mysql+mysqlconnector://user_coffee:rootroot@localhost/coffee')
print(type(engine), engine)

"""
    Define the MySQL engine using MySQL Connector/Python
    mysql+mysqlconnector://user:password@host:port/default_db
    echo=True는 SQLAlchemy가 실행하는 각 SQL 문을 인쇄. 테스트 할 때 유용
    
    echo=True플래그 대신 Python 로깅을 사용하여 SQL 쿼리를 로깅하려면 다음을 수행하십시오 .

    import logging
    
    logging.basicConfig()
    logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)
    
"""
engine = sqlalchemy.create_engine('mysql+mysqlconnector://user_coffee:rootroot@localhost:3306/coffee', echo=True)
print(type(engine), engine)