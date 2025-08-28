from locators import Locators
from generate_user import generate_email, generate_password
from conftest import browser
from urls import LOGIN_PAGE

class TestLoginFunctionality:
    def test_login_from_homepage(self, browser):
        browser.get(LOGIN_PAGE)
        email_field = browser.find_element(*Locators.EMAIL_FIELD)
        password_field = browser.find_element(*Locators.PASSWORD_FIELD)
        submit_button = browser.find_element(*Locators.SUBMIT_BUTTON)

        valid_email = generate_email()
        valid_password = generate_password()

        email_field.send_keys(valid_email)
        password_field.send_keys(valid_password)
        submit_button.click()

        account_link = browser.find_element(*Locators.PERSONAL_ACCOUNT_LINK)
        assert account_link.is_displayed(), "Логин прошел неудачно"

    def test_login_from_forgotten_password_page(self, browser):
        browser.get(FORGOTTEN_PASSWORD_PAGE)
        back_to_login_button = browser.find_element(*Locators.LOGIN_BACK_BUTTON)
        back_to_login_button.click()

        email_field = browser.find_element(*Locators.EMAIL_FIELD)
        password_field = browser.find_element(*Locators.PASSWORD_FIELD)
        submit_button = browser.find_element(*Locators.SUBMIT_BUTTON)

        valid_email = generate_email()
        valid_password = generate_password()

        email_field.send_keys(valid_email)
        password_field.send_keys(valid_password)
        submit_button.click()

        account_link = browser.find_element(*Locators.PERSONAL_ACCOUNT_LINK)
        assert account_link.is_displayed(), "Логин прошел неудачно"