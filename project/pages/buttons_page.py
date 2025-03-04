from .base_page import BasePage
from selenium.webdriver.common.by import By

class ButtonsPage(BasePage):
    BUTTON_1 = (By.ID, "button1")
    BUTTON_2 = (By.ID, "button2")
    BUTTON_3 = (By.ID, "button3")
    BUTTON_4 = (By.ID, "button4")
    MESSAGE = (By.ID, "demo")

    def click_button_1(self):
        self.click(self.BUTTON_1)

    def click_button_2(self):
        self.click(self.BUTTON_2)

    def click_button_3(self):
        self.click(self.BUTTON_3)

    def click_button_4(self):
        self.click(self.BUTTON_4)

    def get_message_text(self):
        return self.get_text(self.MESSAGE)