# import allure
# from selenium import webdriver
#
# from models.user import UserAccountResponse
# from utils.api.api_facade import ApiFacade
#
#
# class AuthorizationApi:
#
#     def __init__(self, base_url, driver: webdriver, api_clients: dict[str, ApiFacade]):
#         self.driver = driver
#         self.api_clients = api_clients
#         self.host = base_url
#
#     def open_page(self, route: str = None):
#         url = f"{self.host}{route}" if route else f"{self.host}"
#         self.driver.get(url)
#
#     def set_cookie(self, user: UserAccountResponse):
#         value = self.api_clients[user.userId].account.auth_token
#         cookie = {
#             'name': 'token',
#             'value': value}
#         self.driver.add_cookie(cookie)
#
#     def refresh_page(self):
#         with allure.step("Перезагрузить страницу"):
#             self.driver.refresh()
#
#     def open_page_with_auth(self, route: str, user):
#         self.open_page(route)
#         self.set_cookie(user)
#         self.refresh_page()
