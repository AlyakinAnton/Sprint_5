from selenium.webdriver.common.by import By
from locators import Locators
from conftest import browser
from urls import CONSTRUCTOR_PAGE

class TestConstructorNavigation:
    def test_navigate_buns_section(self, browser):
        browser.get(CONSTRUCTOR_PAGE)
        buns_section = browser.find_element(*Locators.BUNS_SECTION)
        buns_section.click()
        section_title = browser.find_element(By.TAG_NAME, "h2").text
        assert "Булки" in section_title, "Раздел булок не открылся"

    def test_navigate_sauces_section(self, browser):
        browser.get(CONSTRUCTOR_PAGE)
        sauces_section = browser.find_element(*Locators.SAUCES_SECTION)
        sauces_section.click()
        section_title = browser.find_element(By.TAG_NAME, "h2").text
        assert "Соусы" in section_title, "Раздел соусов не открылся"

    def test_navigate_fillings_section(self, browser):
        browser.get(CONSTRUCTOR_PAGE)
        fillings_section = browser.find_element(*Locators.FILLINGS_SECTION)
        fillings_section.click()
        section_title = browser.find_element(By.TAG_NAME, "h2").text
        assert "Начинки" in section_title, "Раздел начинок не открылся"