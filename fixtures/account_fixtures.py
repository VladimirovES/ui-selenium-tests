import pytest

from data_test.user_data import UserData
from utils.api.account_api import AccountApi
from utils.api.api_facade import ApiFacade


@pytest.fixture(scope='session')
def create_user_for_login(base_url):
    user = UserData.user_changes
    user.userId = AccountApi(base_url=base_url, module='Account').create_user(user)['userID']
    api_client = ApiFacade(base_url=base_url, auth_token=user.token)
    yield user
    api_client.account.delete_user(user)
