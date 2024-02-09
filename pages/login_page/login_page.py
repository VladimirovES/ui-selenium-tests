from selenium import webdriver
from selenium.webdriver.common.by import By

from models.user import UserAccount
from pages.base.base_component import Button, Text, Input

from pages.base.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, driver: webdriver, base_url):
        super().__init__(driver, base_url)

        self.username = Input(self._driver,
                              locator=(By.XPATH, "//input[@id='userName']"),
                              name='UserName')
        self.password = Input(self._driver, locator=(By.XPATH, "//input[@id='password']"), name='Password')
        self.login = Button(self._driver, locator=(By.XPATH, "//button[@id='login']"), name='Login')
        self.validation_error = Text(self._driver, locator=(By.XPATH, "//p[@class='mb-1']"),
                                     name='Invalid Login or Password')

    def open_page(self, route='login'):
        super().open_page(route)

    def sign_in(self, login, password):
        self.username.fill(text=login)
        self.password.fill(text=password)
        self.login.click()
