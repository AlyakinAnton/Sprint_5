from selenium import webdriver
from selenium.webdriver.common.by import By
from locators import Locators
from generate_user import generate_email, generate_password


def test_successful_registration():
    try:
        driver = webdriver.Chrome()

        driver.get("https://stellarburgers.nomoreparties.site/")
        register_button = driver.find_element(*Locators.REGISTER_BUTTON)
        register_button.click()

        name_field = driver.find_element(*Locators.NAME_FIELD)
        email_field = driver.find_element(*Locators.EMAIL_FIELD)
        password_field = driver.find_element(*Locators.PASSWORD_FIELD)
        submit_button = driver.find_element(*Locators.SUBMIT_BUTTON)

        unique_email = generate_email()
        strong_password = generate_password()

        name_field.send_keys("Test User")
        email_field.send_keys(unique_email)
        password_field.send_keys(strong_password)
        submit_button.click()

        assert driver.current_url != "/register", "Ошибка успешной регистрации."
    finally:
        driver.quit()