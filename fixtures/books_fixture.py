import pytest

from data_test.user_data import UserData


@pytest.fixture()
def add_book(request, api_clients):
    book = request.param
    api_clients[UserData.user1.userId].books.post_book_store(user=UserData.user1,
                                                             book=book)
    yield book
    api_clients[UserData.user1.userId].books.delete_book(user=UserData.user1,
                                                         book=book)
