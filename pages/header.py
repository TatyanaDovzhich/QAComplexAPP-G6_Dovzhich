from enum import verify

from constants.header import HeaderConsts
from pages.base_page import BasePage
from pages.utils import log_wrapper, wait_until_ok


class Header(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.const = HeaderConsts

    @wait_until_ok(timeout=3, period=0.5)
    def click_and_validate_create_post_button(self):
        """Click on Create Post button until it disappear"""
        self.click(self.const.CREATE_POST_BUTTON_XPATH)
        assert not self.is_element_exists(self.const.CREATE_POST_BUTTON_XPATH), "Create Post button didn't disappear"

    @log_wrapper
    def create_post_button(self, username, password):
        """Click on Create Post button"""
        if verify:
            self.click_and_validate_create_post_button()
        else:
            self.click(self.const.CREATE_POST_BUTTON_XPATH)

    @wait_until_ok(timeout=3, period=0.5)
    def click_and_validate_sign_out_button(self):
        """Click on Sign Out button until it disappear"""
        self.click(self.const.SIGN_OUT_BUTTON_XPATH)
        assert not self.is_element_exists(self.const.SIGN_OUT_BUTTON_XPATH), "Sign Out button didn't disappear"

    @log_wrapper
    def sign_out_button(self, username, password):
        """Click on Sign Out button"""
        if verify:
            self.click_and_validate_sign_out_button()
        else:
            self.click(self.const.SIGN_OUT_BUTTON_XPATH)

    @log_wrapper
    def navigate_to_create_post(self):
        """Navigate to create post page via header Create Post button"""
        self.click(xpath=self.const.CREATE_POST_BUTTON_XPATH)

    @log_wrapper
    def navigate_to_start_page(self):
        """Navigate to Start Page via header Sign Out button"""
        self.click(xpath=self.const.SIGN_OUT_BUTTON_XPATH)

        from pages.start_page import StartPage
        return StartPage(self.driver)

    @wait_until_ok(timeout=3, period=0.5)
    def click_and_validate_my_profile_button(self):
        """Click on My Profile button until it disappear"""
        self.click(self.const.MY_PROFILE_BUTTON_XPATH)
        assert not self.is_element_exists(self.const.MY_PROFILE_BUTTON_XPATH), "My Profile button didn't disappear"

    @log_wrapper
    def my_profile_button(self, username, password):
        """Click on My Profile button"""
        if verify:
            self.click_and_validate_my_profile_button()
        else:
            self.click(self.const.MY_PROFILE_BUTTON_XPATH)

    @log_wrapper
    def navigate_to_profile_page(self):
        """Navigate to Profile Page via header My Profile button"""
        self.click(xpath=self.const.MY_PROFILE_BUTTON_XPATH)

        from pages.profile_page import ProfilePage
        return ProfilePage(self.driver)
