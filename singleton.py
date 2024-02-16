from utils.driver_factory import DriverFactory


class BaseUrlSingleton:
    _instance = None
    base_url = ""

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    @classmethod
    def set_base_url(cls, url):
        cls.get_instance().base_url = url

    @classmethod
    def get_base_url(cls):
        return cls.get_instance().base_url

class BrowserSingleton:
    _instance = None
    _driver = None
    browser_name = "chrome"
    headless = False
    remote = False
    executor_url = "http://selenoid:4444/wd/hub"

    @classmethod
    def setup(cls, request):
        # Инициализация параметров из конфигурации pytest
        cls.browser_name = request.config.getoption('--browser_name')
        cls.headless = request.config.getoption('--headless')
        cls.remote = request.config.getoption('--remote_browser')
        cls.executor_url = request.config.getoption('--executor')

    @classmethod
    def get_driver(cls):
        if cls._instance is None:
            cls._instance = cls()
            driver_factory = DriverFactory(browser_name=cls.browser_name,
                                           headless=cls.headless,
                                           remote=cls.remote,
                                           executor_url=cls.executor_url)
            cls._driver = driver_factory.get_driver()
            cls._driver.delete_all_cookies()
        return cls._driver

    @classmethod
    def quit_driver(cls):
        if cls._driver:
            cls._driver.quit()
            cls._driver = None
            cls._instance = None




