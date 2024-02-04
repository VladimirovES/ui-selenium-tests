from selenium.webdriver.common.by import By

from models.user import User
from pages.base.base_component import Button, Input, Iframe
from pages.base.base_page import BasePage
from utils.routing import Routing


class RegistrationPage(BasePage):
    def __init__(self, driver, base_url):
        super().__init__(driver, base_url)

    def open_page(self, route=Routing.register):
        super().open_page(route=route)

        self.first_name = Input(self._driver,
                                locator=(By.XPATH, "//input[@id='firstname']"),
                                name='FirstName')
        self.last_name = Input(self._driver,
                               locator=(By.ID, "lastname"),
                               name='LastName')
        self.user_name = Input(self._driver,
                               locator=(By.CSS_SELECTOR, "input[id='userName']"),
                               name='UserName')
        self.password = Input(self._driver, locator=(By.XPATH, "//input[@id='password']"),
                              name='Password')
        self.captcha_iframe = Iframe(self._driver, locator=(By.XPATH, "//iframe[@title='reCAPTCHA']"),
                                     name='Iframe Captcha')
        self.checkbox_captcha = Button(self._driver,
                                       locator=(By.XPATH, "//*[@role='checkbox']"),
                                       name='Чек-бокс капчи')
        self.register = Button(self._driver, locator=(By.XPATH, "//button[@id='register"),
                               name='Register')

    def captcha_checkbox_click(self):
        self.captcha_iframe.switch_to_iframe()
        self.checkbox_captcha.click()

    def registration_user(self, user: User):
        self.first_name.fill(text=user.first_name)
        self.last_name.fill(text=user.last_name)
        self.password.fill(text=user.password)
        self.user_name.fill(text=user.user_name)
        self.captcha_checkbox_click()
        self.register.click()
