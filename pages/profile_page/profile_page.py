from selenium import webdriver
from selenium.webdriver.common.by import By

from pages.base.base_component import Button
from pages.base.base_page import BasePage


class ProfilePage(BasePage):
    def __init__(self, driver: webdriver, base_url):
        super().__init__(driver, base_url)

    def open_page(self, route='profile'):
        super().open_page(route)

        self.log_out = Button(self._driver,
                              locator=(By.XPATH, "//button[@id='submit']"),
                              name='Log out')

