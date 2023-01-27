"""Tests related to hello page"""
import logging

import pytest


class TestHelloPage:
    """Stores tests for create hello page base functionality"""

    log = logging.getLogger("[TestHelloPage]")

    @pytest.fixture()
    def test_sign_out_from_hello_page_after_sign_in(self, start_page, random_login):
        """
        - Pre-conditions:
            - Sign In as a user
        - Steps:
            - Click on "Sign Out" button
            - Navigate to start page
        """
        # Sign In as a user
        hello_page = start_page.sign_in(random_login)

        # Verify login success
        hello_page.verify_sign_up_message(username=random_login.username_value)

        # Click on "Sign Out" button
        hello_page.header.sign_out_button()

        # Navigate to start page
        start_page = hello_page.navigate_to_start_page()
        return start_page

    @pytest.fixture()
    def test_sign_out_from_hello_page_after_sign_up(self, start_page, random_user):
        """
         - Pre-conditions:
            - Open start page
            - Sign Up as the user
        - Steps:
            - Click on Sign Out Button
            - Verify the result (Navigate to start page)
        """
        # Sign Up as a user
        hello_page = start_page.sign_up(random_user)

        # Verify login success
        hello_page.verify_sign_up_message(username=random_user.username_value)

        # Click on "Sign Out" button
        hello_page.header.sign_out_button()

        # Navigate to start page
        start_page = hello_page.navigate_to_start_page()
        return start_page
