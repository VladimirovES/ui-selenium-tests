from typing import List
from pydantic import BaseModel


class Isbn(BaseModel):
    isbn: str


class UserIsbns(BaseModel):
    userId: str
    collectionOfIsbns: List[Isbn]
