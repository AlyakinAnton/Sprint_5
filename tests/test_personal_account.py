from locators import Locators
from conftest import browser
from urls import PERSONAL_ACCOUNT_PAGE

class TestPersonalAccountNavigation:
    def test_navigation_to_personal_account(self, browser):
        browser.get(PERSONAL_ACCOUNT_PAGE)
        profile_link = browser.find_element(*Locators.PROFILE_LINK)
        profile_link.click()

        current_url = browser.current_url
        assert current_url.endswith("/account/profile"), "Переход в Личный кабинет не состоялся"

    def test_logout(self, browser):
        browser.get(PERSONAL_ACCOUNT_PAGE)
        logout_button = browser.find_element(*Locators.LOGOUT_BUTTON)
        logout_button.click()

        login_button = browser.find_element(*Locators.LOGIN_BUTTON)
        assert login_button.is_displayed(), "Пользователь не покинул аккаунт"