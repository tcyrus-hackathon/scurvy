from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

engine = create_engine('sqlite:///database.db', echo=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(120), unique=True)
    email = Column(String(120), unique=True)
    password = Column(String(30))
    num = Column(Integer)

    def __init__(self, name=None, email=None, password=None, num=None):
        self.name = name
        self.email = email
        self.password = password
        self.num = num

    def __repr__(self):
        return '<User %r>' % (self.name)

Base.metadata.create_all(bind=engine)
