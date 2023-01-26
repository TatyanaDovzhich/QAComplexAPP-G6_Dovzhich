from enum import verify

from constants.create_post_page import CreatePostPageConsts
from pages.base_page import BasePage
from pages.header import Header
from pages.utils import wait_until_ok, log_wrapper


class CreatePostPage(BasePage):
    """Stores methods describes create post page actions"""

    def __init__(self, driver):
        super().__init__(driver)
        self.const = CreatePostPageConsts
        self.header = Header(self.driver)

    @wait_until_ok(timeout=3, period=0.5)
    def click_and_validate_save_post_button(self):
        """Click on Save Post button until it disappear"""
        self.click(self.const.SAVE_POST_BUTTON_XPATH)
        assert not self.is_element_exists(self.const.SAVE_POST_BUTTON_XPATH), "Save Post button didn't disappear"

    @log_wrapper
    def create_post(self, title, body):
        """Create post using provided values"""
        self.fill_field(xpath=self.const.TITLE_INPUT_XPATH, value=title)
        self.fill_field(xpath=self.const.BODY_AREA_XPATH, value=body)
        # Click on Save Post button
        if verify:
            self.click_and_validate_save_post_button()
        else:
            self.click(self.const.SAVE_POST_BUTTON_XPATH)

    @log_wrapper
    def navigate_to_post_page(self):
        """Navigate to post page via Save Post button"""
        self.click(xpath=self.const.SAVE_POST_BUTTON_XPATH)

        from pages.post_page import PostPage
        return PostPage(self.driver)
