from datetime import datetime
from booknetwork import Base, db
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String)
    email = Column(String)
    password = Column(String)
    user_reviews = relationship("Review")

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

class Review(Base):
    __tablename__ = 'reviews'
    
    id = Column(Integer, primary_key=True)
    content = Column(String)
    date_posted = Column(String)
    rating = Column(Integer)
    user_id = Column(Integer, ForeignKey('user.id'))
    book_id = Column(Integer, ForeignKey('book.id'))

    def __init__(self, id, content, date_posted, rating, user_id, book_id):
        self.id = id
        self.content = content
        self.date_posted = date_posted
        self.rating = rating
        self.user_id = user_id
        self.book_id = book_id

class Book(Base):
    __tablename__ = 'book'
    id = Column(Integer, primary_key=True)
    isbn = Column(String)
    title = Column(String)
    author = Column(String)
    pub_date = Column(Integer)
    book_reviews = relationship('Review')

    def __init__(self, id, isbn, title, author, pub_date):
        self.id = id
        self.isbn = isbn
        self.title = title
        self.author = author
        self.pub_date = pub_date
