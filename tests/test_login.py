import allure

from data_test.user_data import UserData
from singletons import BaseUrlSingleton
from utils.routing import Routing
import pytest


@pytest.mark.regress
@pytest.mark.login
@allure.epic('User')
@allure.feature('LoginPage')
class TestLogin:

    @allure.story('Login')
    @allure.title('With valid creeds"')
    def test_valid_login(self, app, create_user_for_login):
        # Arrange
        expected_url = BaseUrlSingleton.get_base_url() + f'{Routing.profile}'
        user = create_user_for_login

        # Act
        app.login.open_page()
        app.login.sign_in(login=user.userName, password=user.password)

        # Assert
        app.login.assert_url_window_eql(expected_url)

    @allure.story('Invalid Login')
    @allure.title('With username "{login}" and password "{password}"')
    @pytest.mark.parametrize('login, password', [(UserData.user_changes.userName, 'invalid'),
                                                 ('invalid_login', UserData.user_changes.password),
                                                 (UserData.user_changes.userName, ""),
                                                 ("", UserData.user_changes.password),
                                                 ("", ""),
                                                 ('invalid', 'invalid')])
    def test_invalid_login(self, app, create_user_for_login, login, password):
        # Act
        app.login.open_page()
        app.login.sign_in(login=login, password=password)

        # Assert
        app.login.validation_error.assert_text_eql('Invalid username or password!')
