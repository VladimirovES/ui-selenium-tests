from selenium import webdriver
from selenium.webdriver.common.by import By

from pages.base.base_component import Button, Text, Input
from pages.base.base_page import BasePage


class ProfilePage(BasePage):
    def __init__(self, driver: webdriver, base_url):
        super().__init__(driver, base_url)

    def open_page(self, route='profile'):
        super().open_page(route)

        self.log_out = Button(self._driver,
                              locator=(By.XPATH, "//button[@id='submit']"),
                              name='Log out')

        self.username = Text(self._driver,
                             locator=(By.XPATH, "//*[@id='userName-value']"),
                             name='username')
        self.delete_account = Button(self._driver,
                                     locator=(
                                         By.XPATH,
                                         "//*[@class='text-right button di']//button[@class='btn btn-primary']"),
                                     name='Delete Account')
        self.input_search_book = Input(self._driver,
                                       locator=(By.XPATH, "//input[@id='searchBox']"),
                                       name='Search Books')
