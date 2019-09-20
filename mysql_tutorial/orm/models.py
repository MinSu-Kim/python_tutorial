from sqlalchemy import Column, Integer, String, DateTime
from database import Base


class TbTest(Base):
    _tablename_ = 'tbTable'
    id = Column(Integer, primary_key=True)
    datetime = Column(DateTime)
    string = Column(String(250))

    def __init__(self, datetime, string):
        self.datetime = datetime
        self.string = string

    def __repr__(self):
        return "<TbTest('%d', '%s', '%s'>" % (self.id, str(self.datetime), self.string)