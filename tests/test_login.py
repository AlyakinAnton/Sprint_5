from selenium import webdriver
from selenium.webdriver.common.by import By
from locators import Locators
from generate_user import generate_email, generate_password

def test_login_from_homepage():
    try:
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/")
        login_button = driver.find_element(*Locators.LOGIN_BUTTON)
        login_button.click()

        email_field = driver.find_element(*Locators.EMAIL_FIELD)
        password_field = driver.find_element(*Locators.PASSWORD_FIELD)
        submit_button = driver.find_element(*Locators.SUBMIT_BUTTON)

        email_field.send_keys(generate_email())
        password_field.send_keys(generate_password())
        submit_button.click()

        personal_account_link = driver.find_element(*Locators.PERSONAL_ACCOUNT_LINK)
        assert personal_account_link.is_displayed(), "Пользователь не вошел успешно."
    finally:
        driver.quit()