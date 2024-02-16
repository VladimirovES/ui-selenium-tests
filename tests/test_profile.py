import allure

import pytest

from data_test.books_data import BooksData
from data_test.user_data import UserData
from utils.routing import Routing


@pytest.mark.regress
@pytest.mark.profile
@allure.epic('User')
@allure.feature('ProfilePage')
class TestProfile:
    @allure.title('Visibility username in profile')
    def test_nickname_user(self, app):
        # Act
        app.profile.auth(user=UserData.user1).open_page()

        # Assert
        app.profile.username.assert_text_eql(expected=UserData.user1.userName)

    @allure.title('Logout')
    def test_logout_user(self, app, base_url):
        # Arrange
        expected_url = base_url + f'{Routing.login}'

        # Act
        app.profile.auth(user=UserData.user2).open_page()
        app.profile.log_out.click()

        # Assert
        app.profile.assert_url_window_eql(expected_url)

    @allure.title('Book present in books table')
    @pytest.mark.parametrize('add_book', [BooksData.book1], indirect=True)
    def test_books_in_profile(self, app, add_book):
        # Act
        app.profile.auth(user=UserData.user1).open_page()

        # Assert
        app.profile.assert_book_in_table(book=add_book)
