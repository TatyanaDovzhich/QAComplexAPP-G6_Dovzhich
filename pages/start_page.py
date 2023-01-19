import logging
from time import sleep

from constants.start_page import StartPageConst
from pages.base_page import BasePage


class StartPage(BasePage):
    """Stores methods describes start page actions"""

    def __init__(self, driver):
        super().__init__(driver)
        self.const = StartPageConst
        self.hello_page = HelloPage
        self.log = logging.getLogger("[StartPage]")

    def sign_in(self, username, password):
        """Sign in using provided values"""
        # Fill fields
        self.fill_field(xpath=self.const.SIGN_IN_USERNAME_FIELD_XPATH, value=username)
        self.fill_field(xpath=self.const.SIGN_IN_PASSWORD_FIELD_XPATH, value=password)
        sleep(1)
        # Click on SignIn button
        self.click(self.const.SIGN_IN_BUTTON_XPATH)
        sleep(1)

    def verify_sign_in_error(self):
        """Verify that text is matches to expected"""
        assert self.compare_element_text(xpath=self.const.SIGN_IN_ERROR_XPATH, text=self.const.SIGN_IN_ERROR_TEXT)

    def sign_up(self, username, email, password):
        """Sign up using provided values"""
        # Fill fields
        self.fill_field(xpath=self.const.SIGN_UP_USERNAME_FIELD_XPATH, value=username)
        self.fill_field(xpath=self.const.SIGN_UP_EMAIL_FIELD_XPATH, value=email)
        self.fill_field(xpath=self.const.SIGN_UP_PASSWORD_FIELD_XPATH, value=password)
        sleep(2)
        # Click on SignUn button
        self.click(self.const.SIGN_UP_BUTTON_XPATH)
        sleep(2)

        from pages.hello_page import HelloPage
        return HelloPage(self.driver)

    def verify_sign_up_username_empty(self):
        """Verify that text is matches to expected"""
        assert self.compare_element_text(xpath=self.const.SIGN_UP_USERNAME_EMPTY_XPATH,
                                         text=self.const.SIGN_UP_USERNAME_EMPTY_TEXT)

    def verify_sign_up_email_empty(self):
        """Verify that text is matches to expected"""
        assert self.compare_element_text(xpath=self.const.SIGN_UP_EMAIL_EMPTY_XPATH,
                                         text=self.const.SIGN_UP_EMAIL_EMPTY_TEXT)

    def verify_sign_up_password_empty(self):
        """Verify that text is matches to expected"""
        assert self.compare_element_text(xpath=self.const.SIGN_UP_PASSWORD_EMPTY_XPATH,
                                         text=self.const.SIGN_UP_PASSWORD_EMPTY_TEXT)

    def verify_sign_up_username_invalid_data(self):
        """Verify that text is matches to expected"""
        assert self.compare_element_text(xpath=self.const.SIGN_UP_USERNAME_INVALID_DATA_XPATH,
                                         text=self.const.SIGN_UP_USERNAME_INVALID_DATA_TEXT)

    def verify_sign_up_email_invalid_data(self):
        """Verify that text is matches to expected"""
        assert self.compare_element_text(xpath=self.const.SIGN_UP_EMAIL_INVALID_DATA_XPATH,
                                         text=self.const.SIGN_UP_EMAIL_INVALID_DATA_TEXT)

    def verify_sign_up_password_invalid_data(self):
        """Verify that text is matches to expected"""
        assert self.compare_element_text(xpath=self.const.SIGN_UP_PASSWORD_INVALID_DATA_XPATH,
                                         text=self.const.SIGN_UP_PASSWORD_INVALID_DATA_TEXT)

    def verify_sign_up_username_exists(self):
        """Verify that text is matches to expected"""
        assert self.compare_element_text(xpath=self.const.SIGN_UP_USERNAME_EXIST_XPATH,
                                         text=self.const.SIGN_UP_USERNAME_EXIST_TEXT)

    def verify_sign_up_email_exists(self):
        """Verify that text is matches to expected"""
        assert self.compare_element_text(xpath=self.const.SIGN_UP_EMAIL_EXIST_XPATH,
                                         text=self.const.SIGN_UP_EMAIL_EXIST_TEXT)
