from constants.profile_page import ProfilePageConsts
from pages.base_page import BasePage
from pages.header import Header
from pages.utils import log_wrapper


class ProfilePage(BasePage):
    """Stores methods describes profile page actions"""

    def __init__(self, driver):
        super().__init__(driver)
        self.const = ProfilePageConsts
        self.header = Header(self.driver)

    @log_wrapper
    def verify_profile_page_message(self, username):
        """Verify Profile Page message"""
        assert self.compare_element_text(
            xpath=self.const.PROFILE_MESSAGE_XPATH, text=f"{username.lower()}"
        )
        assert self.compare_element_text(xpath=self.const.USERNAME_IN_PROFILE_MESSAGE_XPATH, text=username.lower())
