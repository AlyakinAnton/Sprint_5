from selenium.webdriver.common.by import By

class Locators:
    LOGIN_BUTTON = (By.XPATH, "//button[contains(text(), 'Войти')]")  # Кнопка войти
    REGISTER_BUTTON = (By.XPATH, "//a[@href='/register']")  # Кнопка Регистрация
    FORGOT_PASSWORD_LINK = (By.XPATH, "//a[@href='/forgot-password']")  # Ссылка Забыл пароль

    NAME_FIELD = (By.NAME, "name")  # Поле Имя
    EMAIL_FIELD = (By.NAME, "email")  # Поле Email
    PASSWORD_FIELD = (By.NAME, "password")  # Поле Пароль
    SUBMIT_BUTTON = (By.XPATH, "//button[contains(text(), 'Зарегистрироваться')]")  # Кнопка Зарегистрироваться

    PERSONAL_ACCOUNT_LINK = (By.XPATH, "//a[@href='/account/profile']")  # Ссылка Личный кабинет
    CONSTRUCTOR_LINK = (By.XPATH, "//a[@href='/constructor']")  # Ссылка Конструктор
    LOGO_STELLAR_BURGER = (By.CLASS_NAME, "App_logo__hBwVd")  # Логотип Stellar Burger

    BUNS_SECTION = (By.XPATH, "//span[contains(text(), 'Булки')]")  # Раздел Булки
    SAUCES_SECTION = (By.XPATH, "//span[contains(text(), 'Соусы')]")  # Раздел Соусы
    FILLINGS_SECTION = (By.XPATH, "//span[contains(text(), 'Начинки')]")  # Раздел Начинки

    EXIT_BUTTON = (By.XPATH, "//button[contains(text(), 'Выйти')]")  # Кнопка Выход