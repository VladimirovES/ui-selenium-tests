import logging

import pytest

from data_test.user_data import UserData
from logging_config import configure_logging
from utils.api.account_api import AccountApi
from utils.api.api_facade import ApiFacade

configure_logging()

logger = logging.getLogger(__name__)


@pytest.fixture()
def create_user_for_login(base_url):
    user = UserData.user_changes
    user.userId = ApiFacade(base_url=base_url).account.create_user(user)['userID']
    yield user
    user.token = AccountApi(base_url=base_url, module='Account').generate_token(user=user)[
        'token']
    ApiFacade(base_url=base_url, auth_token=user.token).account.delete_user(user)
