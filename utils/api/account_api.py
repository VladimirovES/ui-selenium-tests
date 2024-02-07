from http import HTTPStatus

from models.user import UserAccount
from utils.api.api_base import ApiClient


class AccountApi(ApiClient):
    auth = 'authorized'
    user = 'user'
    gen_token = 'GenerateToken'

    def auth_user(self, user: UserAccount):
        return self.post(end_point=self.auth, payload={'userName': user.userName,
                                                       'password': user.password}, expected_status=HTTPStatus.OK)

    def create_user(self, user: UserAccount):
        return self.post(end_point=self.user,
                         payload={'userName': user.userName,
                                  'password': user.password})

    def generate_token(self, user: UserAccount):
        r = self.post(end_point=self.gen_token, payload={'userName': user.userName,
                                                         'password': user.password}, expected_status=HTTPStatus.OK)
        try:
            self.auth_token = r['token']
        except KeyError:
            self.auth_token = None
            print(f"Error Auth: key 'token' is not present in JSON - Response. {r}")
        return r

    def delete_user(self, user: UserAccount):
        return self.delete(end_point=self.user + f'/{user.userId}')
