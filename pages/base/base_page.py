import allure
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from models.user import UserAccount
from singleton import BaseUrlSingleton
from utils.assertions import assert_data_is_equal


class BasePage:

    def __init__(self, driver: webdriver):
        self._driver = driver
        self.host = BaseUrlSingleton.get_base_url()

    def open_page(self, route: str = None):
        url = f"{self.host}{route}" if route else f"{self.host}"
        with allure.step(f"Открыть страницу {url}"):
            self._driver.get(url)

    def auth(self, user: UserAccount):
        with allure.step(f"Добавить куки для пользователя: {user.userName}"):
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

    def switch_to_next_window(self, index_window: int = -1):
        last_window = self._driver.window_handles[index_window]
        self._driver.switch_to.window(last_window)

    def assert_url_window_eql(self, url: str, index_window: int = 0):
        self.switch_to_next_window(index_window)
        self._wait_for_url_to_be(url)
        assert_data_is_equal(url, self.get_page_url(), name='URL открытой страницы совпадает')

    def _wait_for_url_to_be(self, url: str, timeout: int = 10):
        try:
            WebDriverWait(self._driver, timeout).until(EC.url_to_be(url))
        except TimeoutException:
            raise AssertionError(f"URL не совпадает с ожидаемым {url} после ожидания {timeout} секунд.")
