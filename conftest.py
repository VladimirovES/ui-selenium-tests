import allure

from fixtures.account_fixtures import *
from fixtures.books_fixture import *
from data_test.user_data import UserData
from pages.base.app_facade import AppFacade
from singleton import BaseUrlSingleton, BrowserSingleton
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
def browser():
    driver = BrowserSingleton.get_driver()
    yield driver
    BrowserSingleton.quit_driver()


@pytest.fixture(scope='session', autouse=True)
def setup_browser_singleton(request):
    BrowserSingleton.setup(request)


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
def api_clients():
    user_clients = {}

    for user in [UserData.user1, UserData.user2]:
        user.userId = AccountApi(module='Account').create_user(user)['userID']
        user.token = AccountApi(module='Account').generate_token(user=user)['token']
        api_client_instance = ApiFacade(auth_token=user.token)

        user_clients[user.userId] = api_client_instance

    yield user_clients

    for user in [UserData.user1, UserData.user2]:
        user_clients[user.userId].account.delete_user(user)


@pytest.fixture()
def app() -> AppFacade:
    return AppFacade()


@pytest.fixture(scope="session", autouse=True)
def setup_base_url(request):
    base_url = request.config.getoption("--base_url")
    BaseUrlSingleton.set_base_url(base_url)
