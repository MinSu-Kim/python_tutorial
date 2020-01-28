from sqlalchemy import create_engine, select, func

from sqlalchemy_tutorial.tutorialspoint.using_multiple_tables import students

engine = create_engine('mysql+mysqlconnector://user_coffee:rootroot@localhost/coffee?use_pure=True', echo=True)
con = engine.connect()

result = con.execute(select([func.now()]))
print (result.fetchone())

result = con.execute(select([func.count(students.c.id)]))
print (result.fetchone())