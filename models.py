from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship

from database import BaseModel


class Author(BaseModel):
    __tablename__ = 'author'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False, unique=True)
    bio = Column(String(255), nullable=False)


class Book(BaseModel):
    __tablename__ = "book"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    summary = Column(String(255), nullable=False)
    publication_date = Column(Date(), nullable=False)
    author_id = Column(Integer, ForeignKey("author.id"))

    author = relationship(Author)