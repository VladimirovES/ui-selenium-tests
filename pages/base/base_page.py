import allure
from selenium import webdriver

from models.user import UserAccount


class BasePage:

    def __init__(self, driver: webdriver, base_url):
        self._driver = driver
        self.host = base_url

    def open_page(self, route: str = None):
        url = f"{self.host}{route}" if route else f"{self.host}"
        with allure.step(f"Открыть страницу {url}"):
            self._driver.get(url)

    def auth(self, user: UserAccount):
        with allure.step(f"Добавить куки для пользователя: {user.userId}"):
            self._driver.get(self.host)
            cookies = {'token': user.token,
                       'userID': user.userId,
                       'userName': user.userName,
                       'expires': '2025-02-11T16%3A33%3A08.160Z'}

            for k, v in cookies.items():
                cookie = {'name': k,
                          'value': v}
                self._driver.add_cookie(cookie)
            return self

    def refresh_page(self):
        with allure.step("Перезагрузить страницу"):
            self._driver.refresh()

    def close_page(self):
        with allure.step("Закрыть страницу"):
            self._driver.close()

    def get_page_url(self):
        return self._driver.execute_script("return (()=> { return window.location.href})()")

    def switch_to_next_window(self):
        last_window = self._driver.window_handles[-1]
        self._driver.switch_to.window(last_window)
