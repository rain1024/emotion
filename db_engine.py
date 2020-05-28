from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class Emotion(Base):
    __tablename__ = 'emotion'
    id = Column(Integer, primary_key=True)
    name = Column(String)


engine = create_engine('sqlite:///db')

session = sessionmaker()
session.configure(bind=engine)
s = session()

if __name__ == '__main__':
    emotions = s.query(Emotion).all()
    print(0)
