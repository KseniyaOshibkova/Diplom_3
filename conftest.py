import pytest

import helpers
from api.api_client import ApiClient
from api.api_user import UserApi
from data.url import Url
from helpers import DriverFactory
from pages.forgot_password_page import ForgotPasswordPage
from pages.personal_account_page import PersonalAccountPage


def pytest_addoption(parser):
    """Параметр командной строки --browser"""
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Браузер для запуска тестов: chrome или firefox")


@pytest.fixture
def driver(request):
    """Фикстура для инициализации и закрытия браузера"""
    browser = request.config.getoption("--browser")
    driver = DriverFactory.get_driver(browser)
    driver.maximize_window()
    driver.get(Url.BASE_URL)
    yield driver
    driver.quit()


@pytest.fixture
def client():
    return ApiClient()


@pytest.fixture
def user_api(client):
    return UserApi(client)


@pytest.fixture(scope='function', autouse=False)
def forgot_password(driver):
    return ForgotPasswordPage(driver)


@pytest.fixture(scope='function', autouse=False)
def personal_account(driver):
    return PersonalAccountPage(driver)


@pytest.fixture
def created_user(user_api):
    """Создаёт пользователя через API и удаляет его после теста"""
    user_data = {
        "email": helpers.random_email(),
        "password": "Pass1234",
        "name": "TestUser"}
    create_response = user_api.create_user(user_data)
    body = create_response.json()
    token = body.get("accessToken")

    yield user_data  # логин в тесте через UI

    if token:
        user_api.delete_user(token)
