import pytest
from selenium import webdriver
from pages.buttons_page import ButtonsPage

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture
def buttons_page(driver):
    page = ButtonsPage(driver)
    driver.get("https://practice-automation.com/click-events/")
    return page

def test_button_1(buttons_page):
    buttons_page.click_button_1()
    assert buttons_page.get_message_text() == "Button 1 was clicked!"

def test_button_2(buttons_page):
    buttons_page.click_button_2()
    assert buttons_page.get_message_text() == "Button 2 was clicked!"

def test_button_3(buttons_page):
    buttons_page.click_button_3()
    assert buttons_page.get_message_text() == "Button 3 was clicked!"

def test_button_4(buttons_page):
    buttons_page.click_button_4()
    assert buttons_page.get_message_text() == "Button 4 was clicked!"