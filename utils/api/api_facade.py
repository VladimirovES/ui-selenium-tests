from utils.api.account_api import AccountApi
from utils.api.books_api import BookStoreApi


class ApiFacade:
    def __init__(self, base_url, auth_token=None):
        self.account = AccountApi(base_url=base_url, module='Account', auth_token=auth_token)
        self.books = BookStoreApi(base_url=base_url, module='Bookstore', auth_token=auth_token)
