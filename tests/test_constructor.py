from selenium import webdriver
from selenium.webdriver.common.by import By
from locators import Locators

def test_navigate_buns_section():
    try:
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/")
        buns_section = driver.find_element(*Locators.BUNS_SECTION)
        buns_section.click()

        current_url = driver.current_url
        assert current_url.endswith("/buns"), "Навигация в раздел булок не удалась."
    finally:
        driver.quit()

def test_navigate_sauces_section():
    try:
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/")
        sauces_section = driver.find_element(*Locators.SAUCES_SECTION)
        sauces_section.click()

        current_url = driver.current_url
        assert current_url.endswith("/sauces"), "Навигация в раздел соусов не удалась."
    finally:
        driver.quit()

def test_navigate_fillings_section():
    try:
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/")
        fillings_section = driver.find_element(*Locators.FILLINGS_SECTION)
        fillings_section.click()

        current_url = driver.current_url
        assert current_url.endswith("/fillings"), "Навигация в раздел начинок не удалась."
    finally:
        driver.quit()