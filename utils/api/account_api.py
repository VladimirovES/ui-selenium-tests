from http import HTTPStatus

from models.user import UserRegistrationResponse, UserAccountResponse
from utils.api.api_base import ApiClient


class AccountApi(ApiClient):
    auth = 'authorized'
    user = 'user'
    gen_token = 'GenerateToken'

    def auth_user(self, user: UserAccountResponse):
        r = self.post(end_point=self.auth, payload={'userName': user.userName,
                                                    'password': user.password}, expected_status=HTTPStatus.OK)
        return r

    def create_user(self, user: UserAccountResponse):
        r = self.post(end_point=self.user,
                      payload={'userName': user.userName,
                               'password': user.password})
        # return UserRegistrationResponse.parse_obj(r)
        return r

    def generate_token(self, user: UserAccountResponse):
        r = self.post(end_point=self.gen_token, payload={'userName': user.userName,
                                                    'password': user.password}, expected_status=HTTPStatus.OK)
        try:
            self.auth_token = r['token']
        except KeyError:
            self.auth_token = None
            print(f"Error Auth: key 'token' is not present in JSON - Response. {r}")
        return r
