import pytest
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
def test_user():
    api = ApiClient()
    user_data = api.create_user("test_user@example.com", "123456")
    yield user_data   # передаём в тест
    api.delete_user(user_data["id"])





@pytest.fixture
def created_existing_user(user_api):
    """Создаёт пользователя EXISTING_USER и удаляет его после теста"""
    user_data = DataForUser.EXISTING_USER
    response = user_api.create_user(user_data)
    body = response.json()

    # Возвращает данные пользователя
    yield user_data

    # Удаляет пользователя
    if "accessToken" in body:
        user_api.delete_user(body["accessToken"])

@pytest.fixture
def auth_user_token(user_api: UserApi):
    """Создаёт пользователя AUTH_USER для авторизации, возвращает токен и удаляет после теста"""
    response = user_api.create_user(DataForUserChange.AUTH_USER)
    body = response.json()

    # достаёт токен
    token = body.get("accessToken")

    yield token

    # удаляет пользователя после теста
    if token:
        user_api.delete_user(token)

