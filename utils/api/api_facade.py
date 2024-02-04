from utils.api.account_api import AccountApi


class ApiFacade:
    def __init__(self, base_url, auth_token):
        self.account = AccountApi(base_url=base_url, module='Account', auth_token=auth_token)
