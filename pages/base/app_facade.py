from pages.login_page.login_page import LoginPage
from pages.profile_page.profile_page import ProfilePage


class AppFacade:
    def __init__(self, browser, base_url):
        self.login = LoginPage(browser, base_url)
        self.profile = ProfilePage(browser, base_url)
