import logging

import pytest

from data_test.user_data import UserData
from logging_config import configure_logging
from utils.api.account_api import AccountApi
from utils.api.api_facade import ApiFacade

configure_logging()

logger = logging.getLogger(__name__)


@pytest.fixture()
def create_user_for_login():
    user = UserData.user_changes
    user.userId = ApiFacade().account.create_user(user)['userID']
    yield user
    user.token = AccountApi(module='Account').generate_token(user=user)[
        'token']
    ApiFacade(auth_token=user.token).account.delete_user(user)
