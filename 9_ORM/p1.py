#pip install sqlalchemy

from sqlalchemy import create_engine, Column, Integer, String 
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


Base = declarative_base()

class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String)
    author = Column(String)
    year = Column(Integer)
    isbn = Column(String)

    def __repr__(self):
        return f"<Book(title='{self.title}',author='{self.author}')>"

engine = create_engine('sqlite:///library_new.db',echo=True)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

book1 = Book(title="Python 101",author="Kaustubh", year=2025,isbn="1234567890")
session.add(book1)
session.commit()

books = session.query(Book).all()

for book in books:
    print(book)
