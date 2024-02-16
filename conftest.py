import allure

from fixtures.account_fixtures import *
from data_test.user_data import UserData
from pages.base.app_facade import AppFacade
from pages.profile_page.profile_page import ProfilePage
from utils.api.account_api import AccountApi
from utils.api.api_facade import ApiFacade
from utils.driver_factory import DriverFactory
from utils.files import Files

from decouple import config


@pytest.fixture(scope="session")
def base_url(request):
    return request.config.getoption("--base_url")


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help='Браузер для запуска тестов')
    parser.addoption('--headless', action='store_true', default=None,
                     help='Запуск браузера без окна')
    parser.addoption('--base_url', action='store', default=config("HOST"),
                     help='Выберите хост, для работы тестов')
    parser.addoption('--delay', action='store', default=0.1,
                     help='Задержка между шагами')
    parser.addoption('--remote_browser', action='store_true', default=None,
                     help='Запуск тестов через удаленный сервер')
    parser.addoption('--mk_video', action='store_true', default=False,
                     help='Запись видео теста. True для записи')
    parser.addoption('--executor', action='store', default='http://selenoid:4444/wd/hub',
                     help='Адрес на котором расположен сервер.')


@pytest.fixture(scope='session')
def browser(request, base_url, api_client):
    browser_name = request.config.getoption('--browser_name')
    headless = request.config.getoption('--headless')
    remote = request.config.getoption('--remote_browser')
    executor = request.config.getoption('--executor') or "http://selenoid:4444/wd/hub"

    driver_factory = DriverFactory(browser_name=browser_name,
                                   headless=headless,
                                   remote=remote,
                                   executor_url=executor)
    driver = driver_factory.get_driver()
    driver.delete_all_cookies()
    try:
        yield driver
    finally:
        driver.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        try:
            web_driver = item.funcargs.get("browser", None)
            if web_driver:
                Files.create_dirs_results_reports_is_not_exist()

                allure.attach(web_driver.get_screenshot_as_png(), name='ScreenShot',
                              attachment_type=allure.attachment_type.PNG)
        except Exception as e:
            print("Fail to take screenshot: {}".format(e))


@pytest.fixture(scope='session')
def registration_user(base_url):
    user = UserData.user1
    user.userId = AccountApi(base_url=base_url, module='Account').create_user(user)['userID']
    return user


@pytest.fixture(scope='session')
def api_client(base_url, registration_user):
    registration_user.token = AccountApi(base_url=base_url, module='Account').generate_token(user=registration_user)[
        'token']
    api_client = ApiFacade(base_url=base_url, auth_token=registration_user.token)
    yield api_client
    api_client.account.delete_user(registration_user)


@pytest.fixture()
def app(browser, base_url) -> AppFacade:
    return AppFacade(browser, base_url)


