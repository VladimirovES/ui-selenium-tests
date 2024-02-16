from utils.api.account_api import AccountApi
from utils.api.books_api import BookStoreApi


class ApiFacade:
    def __init__(self, auth_token=None):
        self.account = AccountApi(module='Account', auth_token=auth_token)
        self.books = BookStoreApi(module='Bookstore', auth_token=auth_token)
