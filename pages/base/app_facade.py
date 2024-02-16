from pages.login_page.login_page import LoginPage
from pages.profile_page.profile_page import ProfilePage


class AppFacade:
    login: 'LoginPage'
    profile: 'ProfilePage'

    def __init__(self, ):
        self._page_instances = {}

    def __getattr__(self, name):
        if name not in self._page_instances:
            self._page_instances[name] = self._initialize_page(name)
        return self._page_instances[name]

    def _initialize_page(self, name):
        if name == "login":
            return LoginPage()
        elif name == 'profile':
            return ProfilePage()
