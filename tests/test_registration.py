from generate_user import generate_email, generate_password
from locators import Locators
from conftest import browser
from urls import REGISTRATION_PAGE

class TestRegistration:
    def test_successful_registration(self, browser):
        browser.get(REGISTRATION_PAGE)
        name_field = browser.find_element(*Locators.NAME_FIELD)
        email_field = browser.find_element(*Locators.EMAIL_FIELD)
        password_field = browser.find_element(*Locators.PASSWORD_FIELD)
        submit_button = browser.find_element(*Locators.SUBMIT_BUTTON)

        unique_email = generate_email()
        strong_password = generate_password()

        name_field.send_keys("Test User")
        email_field.send_keys(unique_email)
        password_field.send_keys(strong_password)
        submit_button.click()

        success_message = browser.find_element(*Locators.SUCCESS_REGISTRATION_MESSAGE)
        assert success_message.text == "Вы успешно зарегистрировались", "Ошибка успешной регистрации."

    def test_invalid_password_length(self, browser):
        browser.get(REGISTRATION_PAGE)
        name_field = browser.find_element(*Locators.NAME_FIELD)
        email_field = browser.find_element(*Locators.EMAIL_FIELD)
        password_field = browser.find_element(*Locators.PASSWORD_FIELD)
        submit_button = browser.find_element(*Locators.SUBMIT_BUTTON)

        weak_password = "abc"

        name_field.send_keys("Test User")
        email_field.send_keys(generate_email())
        password_field.send_keys(weak_password)
        submit_button.click()

        error_message = browser.find_element(*Locators.ERROR_SHORT_PASSWORD)
        assert error_message.text == "Минимальная длина пароля — 6 символов.", "Ошибка короткой длины пароля не появилась."