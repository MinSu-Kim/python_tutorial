import sqlalchemy
from sqlalchemy import create_engine

print(sqlalchemy.__version__)
engine = create_engine('mysql://user_ncs_coffee:rootroot@localhost/ncs_coffee')
print(type(engine), engine)