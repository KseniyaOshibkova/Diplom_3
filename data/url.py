class Url:
    BASE_URL = "https://stellarburgers.nomoreparties.site"
    FORGOT_PASSWORD_PAGE = f"{BASE_URL}/forgot-password"
    RESET_PASSWORD = f"{BASE_URL}/reset-password"


    CREATE_USER = "/api/auth/register"
    DELETE_USER = "/api/auth/user"
    REGISTER_USER = "/api/auth/register"


    LOGIN_USER = "/api/auth/login"
    LOGOUT_USER = "/api/auth/logout"


    REFRESH_TOKEN = "/api/auth/token"
    REFRESH_DATA_USERS = "/api/auth/user"
