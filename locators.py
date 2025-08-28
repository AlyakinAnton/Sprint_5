from selenium.webdriver.common.by import By

class Locators:
    # Элементы главной страницы
    LOGIN_BUTTON = (By.XPATH, "//button[contains(text(),'Войти')]")
    REGISTER_BUTTON = (By.XPATH, "//a[@href='/register']")
    FORGOT_PASSWORD_LINK = (By.XPATH, "//a[@href='/forgot-password']")

    # Поля формы регистрации
    NAME_FIELD = (By.NAME, "name")
    EMAIL_FIELD = (By.NAME, "email")
    PASSWORD_FIELD = (By.NAME, "password")
    SUBMIT_BUTTON = (By.XPATH, "//button[contains(text(),'Зарегистрироваться')]")

    # Элементы личного кабинета
    PERSONAL_ACCOUNT_LINK = (By.XPATH, "//a[@href='/account/profile']")
    CONSTRUCTOR_LINK = (By.XPATH, "//a[@href='/constructor']")
    LOGOUT_BUTTON = (By.XPATH, "//button[contains(text(),'Выйти')]")

    # Элементы конструктора
    BUNS_SECTION = (By.XPATH, "//div[contains(@class,'tab_tab_type_current')]/..//*[contains(text(),'Булки')]")
    SAUCES_SECTION = (By.XPATH, "//div[contains(@class,'tab_tab_type_current')]/..//*[contains(text(),'Соусы')]")
    FILLINGS_SECTION = (By.XPATH, "//div[contains(@class,'tab_tab_type_current')]/..//*[contains(text(),'Начинки')]")

    # Сообщения ошибок
    ERROR_SHORT_PASSWORD = (By.XPATH, "//p[contains(text(),'Минимальная длина пароля — 6 символов.')]")

    # Сообщения успеха
    SUCCESS_REGISTRATION_MESSAGE = (By.XPATH, "//p[contains(text(),'Вы успешно зарегистрировались')]")