from typing import List
from pydantic import BaseModel


class Isbn(BaseModel):
    isbn: str


class UserIsbns(BaseModel):
    userId: str
    collectionOfIsbns: List[Isbn]


class Book(BaseModel):
    isbn: str
    title: str
    subTitle: str
    author: str
    publish_date: str
    publisher: str
    pages: int
    description: str
    website: str
