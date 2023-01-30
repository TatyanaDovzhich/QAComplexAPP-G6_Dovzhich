"""Tests related to header"""
import logging

import pytest

from constants.base import BaseConstants


@pytest.mark.parametrize("browser", [BaseConstants.CHROME, BaseConstants.FIREFOX])
class TestHeader:
    """Stores tests for create header base functionality"""

    log = logging.getLogger("[TestHeader]")

    @pytest.fixture()
    def hello_page(self, start_page, random_user):
        return start_page.sign_up(random_user)

    def test_sign_out(self, hello_page):
        """
            - Pre-conditions:
                - Open start page
                - Sign Up as the user
            - Steps:
                - Click on Sign Out Button
                - Verify the result
            """
        # Click on Sign Out Button
        start_page = hello_page.header.navigate_to_start_page_via_sign_out()

        # Verify the result
        start_page.verify_sign_in_exists()
