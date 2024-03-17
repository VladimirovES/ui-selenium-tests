from utils.driver_factory import DriverFactory


class WebDriverSingleton:
    _instance = None
    _driver = None

    @classmethod
    def initialize_driver(cls, browser_name, headless, remote, executor):
        if cls._driver is None:
            executor_url = executor or "http://selenoid:4444/wd/hub"
            driver_factory = DriverFactory(browser_name=browser_name,
                                           headless=headless,
                                           remote=remote,
                                           executor_url=executor_url)
            cls._driver = driver_factory.get_driver()
            cls._driver.delete_all_cookies()

    @classmethod
    def get_driver(cls):
        if cls._driver is None:
            raise Exception("Driver not initialized, call initialize_driver first.")
        return cls._driver

    @classmethod
    def quit_driver(cls):
        if cls._driver:
            cls._driver.quit()
            cls._driver = None


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
