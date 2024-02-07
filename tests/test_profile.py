import allure

import pytest

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
        app.profile.auth(user=UserData.user1).open_page()
        app.profile.log_out.click()

        # Assert
        app.profile.assert_url_window_eql(expected_url)
