from models.books import Book
from models.user import UserAccount
from utils.api.api_base import ApiClient


class BookStoreApi(ApiClient):
    _BOOKS = 'books'
    _BOOK = 'book'

    def post_book_store(self, user: UserAccount, book: Book):
        payload = {
            "userId": user.userId,
            "collectionOfIsbns": [
                {
                    "isbn": book.isbn
                }
            ]
        }
        r = self.post(end_point=self._BOOKS, payload=payload)
        return r

    def delete_book(self, user: UserAccount, book: Book):
        return self.delete(end_point=self._BOOK, payload={
            "isbn": book.isbn,
            "userId": user.userId
        })
