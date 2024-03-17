from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

from selenium.webdriver.remote.file_detector import LocalFileDetector


class DriverFactory:
    def __init__(self, browser_name, headless, remote, executor_url):
        self.browser_name = browser_name
        self.headless = headless
        self.remote = remote
        self.executor_url = executor_url or "http://selenoid:4444/wd/hub"

    def get_driver(self):
        if 'chrome' in self.browser_name.lower():
            return self._create_chrome_driver()
        elif 'firefox' in self.browser_name.lower():
            return self._create_firefox_driver()
        else:
            raise ValueError(f"Browser '{self.browser_name}' is not supported.")

    def _create_chrome_driver(self):
        chrome_options = self._get_chrome_options()
        if self.remote:
            driver = webdriver.Remote(
                command_executor=self.executor_url,
                options=chrome_options)
            driver.file_detector = LocalFileDetector()
            return driver
        else:
            return webdriver.Chrome(
                ChromeDriverManager().install(),
                options=chrome_options
            )

    def _create_firefox_driver(self):
        firefox_options = self._get_firefox_options()
        if self.remote:
            driver = webdriver.Remote(
                command_executor=self.executor_url,
                options=firefox_options
            )
            driver.file_detector = LocalFileDetector()
        else:
            return webdriver.Firefox(
                executable_path=GeckoDriverManager().install(),
                options=firefox_options
            )

    def _get_chrome_options(self):
        options = ChromeOptions()
        if self.headless:
            options.add_argument("--headless")

        prefs = {
            "profile.default_content_settings.popups": 0,
            "profile.default_content_setting_values.automatic_downloads": 1
        }
        if self.remote:
            prefs["download.default_directory"] = "/home/selenium/Downloads"

        options.add_experimental_option("prefs", prefs)

        options.add_argument("--disable-notifications")
        options.add_argument("--enable-automation")
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--disable-extensions")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-gpu")
        options.add_argument("--disable-dev-shm-usage")

        caps = DesiredCapabilities.CHROME
        caps['goog:loggingPrefs'] = {'performance': 'ALL', 'browser': 'ALL', 'driver': 'ALL', }
        caps.update({"applicationCacheEnabled": False})
        return options

    def _get_firefox_options(self):
        options = FirefoxOptions()
        if self.headless:
            options.add_argument("--headless")
        options.add_argument("--width=1920")
        options.add_argument("--height=1080")
        options.set_preference("browser.download.folderList", 2)
        options.set_preference("browser.download.useDownloadDir", True)
        options.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/pdf,application/octet-stream")
        options.set_preference("pdfjs.disabled", True)

        return options
