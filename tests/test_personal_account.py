from selenium import webdriver
from selenium.webdriver.common.by import By
from locators import Locators

def test_navigation_to_personal_account():
    try:
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/")
        personal_account_link = driver.find_element(*Locators.PERSONAL_ACCOUNT_LINK)
        personal_account_link.click()

        current_url = driver.current_url
        assert current_url.endswith("/account/profile"), "Переход в Личный кабинет не сработал."
    finally:
        driver.quit()

def test_logout():
    try:
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/account/profile")
        exit_button = driver.find_element(*Locators.EXIT_BUTTON)
        exit_button.click()

        login_button = driver.find_element(*Locators.LOGIN_BUTTON)
        assert login_button.is_displayed(), "Пользователь не вышел из аккаунта."
    finally:
        driver.quit()