from itertools import zip_longest

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from constants.chat import ChatConsts
from pages.base_page import BasePage
from pages.utils import log_wrapper


class Chat(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.constants = ChatConsts()

    @log_wrapper
    def send_message(self, text):
        """Send provided message"""
        self.fill_field(
            xpath=self.constants.CHAT_INPUT_XPATH, value=text + Keys.ENTER
        )

    @log_wrapper
    def verify_messages(self, expected_messages):
        """Verify all sent messages"""
        messages = self.driver.wait_until_displayed(by=By.XPATH, value=self.constants.CHAT_MESSAGES_XPATH)
        for message, expected_messages in zip_longest(messages, expected_messages):
            assert message.text.strip() == expected_messages, f"Actual: {message}, Expected: {expected_messages}"
