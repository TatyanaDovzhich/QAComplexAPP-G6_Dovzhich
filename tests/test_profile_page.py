"""Tests related to profile page"""
import logging

import pytest


class TestProfilePage:
    """Stores tests for profile page base functionality"""

    log = logging.getLogger("[TestProfilePage]")

    @pytest.fixture()
    def test_navigate_to_profile_page_via_sign_in(self, start_page, random_login):
        """
        - Pre-conditions:
            - Sign In as a user
        - Steps:
            - Click on "My Profile" button
            - Navigate to profile page
            - Verify profile username
        """
        # Sign In as a user
        hello_page = start_page.sign_in(random_login)

        # Verify login success
        hello_page.verify_sign_up_message(username=random_login.username)

        # Click on "My Profile" button
        hello_page.header.my_profile_button()

        # Navigate to profile page
        profile_page = hello_page.navigate_to_profile_page()

        # Verify profile username
        profile_page.verify_profile_page_message(username=random_login.username)

    @pytest.fixture()
    def test_navigate_to_profile_page_via_sign_up(self, start_page, random_user):
        """
        - Pre-conditions:
            - Sign Up as a user
        - Steps:
            - Click on "My Profile" button
            - Navigate to profile page
            - Verify profile username
        """
        # Sign Up as a user
        hello_page = start_page.sign_up(random_user)

        # Verify login success
        hello_page.verify_sign_up_message(username=random_user.username)


        # Click on "My Profile" button
        hello_page.header.my_profile_button()

        # Navigate to profile page
        profile_page = hello_page.navigate_to_profile_page()

        # Verify profile username
        profile_page.verify_profile_page_message(username=random_user.username)

    def test_sign_out_from_profile_page_after_sign_in(self, start_page, random_login):
        """
        - Pre-conditions:
            - Sign In as a user
        - Steps:
            - Click on "My Profile" button
            - Navigate to profile page
            - Click on "Sign Out" button
            - Navigate to start page
        """
        # Sign In as a user
        hello_page = start_page.sign_in(random_login)

        # Verify login success
        hello_page.verify_sign_up_message(username=random_login.username)


        # Click on "My Profile" button
        hello_page.header.my_profile_button()

        # Navigate to profile page
        profile_page = hello_page.navigate_to_profile_page()

        # Navigate to start page
        start_page = hello_page.navigate_to_start_page_via_sign_out()
        return start_page
