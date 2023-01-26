"""Tests related to start page"""
import logging

import pytest

from constants.base import BaseConstants


@pytest.mark.parametrize("browser", [BaseConstants.CHROME, BaseConstants.FIREFOX])
class TestStartPage:
    """Stores tests for start page base functionality"""

    log = logging.getLogger("[TestStartPage]")

    def test_valid_login(self, start_page, random_login):
        """
            - Pre-conditions:
            - Open start page
        - Steps:
            - Fill login
            - Fill password
            - Click on SignIn button
            - Verify login is successful
        """
        # Login as valid user
        hello_page = start_page.sign_in(random_login)

        # Verify login success
        hello_page.verify_sign_in_message(username=random_login.username_value)

    def test_invalid_login(self, start_page, random_login):
        """
        - Pre-conditions:
            - Open start page
        - Steps:
            - Fill login with invalid data
            - Fill password with invalid data
            - Click on SignIn button
            - Verify error
        """
        # Login as invalid user
        start_page.sign_in(random_login)

        # Verify error
        start_page.verify_sign_in_error()

    def test_empty_login(self, start_page, empty_login):
        """
        - Pre-conditions:
            - Open start page
        - Steps:
            - Left empty login
            - Left empty password
            - Click on SignIn button
            - Verify error
        """
        # Login as invalid user
        start_page.sign_in(empty_login)

        # Verify error
        start_page.verify_sign_in_error()

    def test_invalid_login_with_empty_login_field(self, start_page, random_login, empty_login):
        """
        - Pre-conditions:
            - Open start page
        - Steps:
            - Stay empty login field
            - Fill password field
            - Click on Sign In button
            - Verify Error Message
        """
        # Login as invalid user
        start_page.sign_in(username=empty_login.username_value, password=random_login.password_value)

        # Verify error
        start_page.verify_sign_in_error()

    def test_invalid_login_with_empty_password_field(self, start_page, random_login, empty_login):
        """
        - Pre-conditions:
            - Open start page
        - Steps:
            - Fill login field
            - Stay empty password field
            - Click on Sign In button
            - Verify Error Message
        """
        # Login as invalid user
        start_page.sign_in(username=random_login.username_value, password=empty_login.password_value)

        # Verify error
        start_page.verify_sign_in_error()

    def test_invalid_login_with_invalid_username(self, start_page, random_login):
        """
        - Pre-conditions:
            - Open start page
        - Steps:
            - Fill login field with invalid data
            - Fill password field
            - Click on Sign In button
            - Verify Error Message
        """
        # Login as invalid user
        start_page.sign_in(username=random_login.username_value, password=random_login.password_value)

        # Verify error
        start_page.verify_sign_in_error()

    def test_invalid_login_with_invalid_password(self, start_page, random_login):
        """
        - Pre-conditions:
            - Open start page
        - Steps:
            - Fill login field
            - Fill password field with invalid data
            - Click on Sign In button
            - Verify Error Message
        """
        # Login as invalid user
        start_page.sign_in(username=random_login.username_value, password=random_login.password_value)

        # Verify error
        start_page.verify_sign_in_error()

    def test_register(self, start_page, random_user):
        """
        - Pre-conditions:
            - Open start page
        - Steps:
            - Fill login, email and password fields
            - Click on Sign Up button
            - Verify registration is successful
        """

        # Fill email, login and password fields
        hello_page = start_page.sign_up(random_user)

        # Verify register success
        hello_page.verify_sign_up_message(username=random_user.username_value)

    def test_empty_fields_register(self, start_page, empty_user):
        """
        - Pre-conditions:
            - Open start page
        - Steps:
            - Stay empty login, email and password fields
            - Click on Sign Up button
            - Verify Error Message
        """
        # Register using empty fields
        start_page.sign_up(empty_user)

        # Verify error
        start_page.verify_sign_up_username_empty()
        start_page.verify_sign_up_email_empty()
        start_page.verify_sign_up_password_empty()

    def test_empty_username_register(self, start_page, random_user, empty_user):
        """
        - Pre-conditions:
            - Open start page
        - Steps:
            - Stay empty username field
            - Fill email and password fields
            - Click on Sign Up button
            - Verify Error Message
        """
        # Register using empty username
        start_page.sign_up(username=empty_user.username_value, email=random_user.email_value,
                           password=random_user.password_value)
        self.log.info("Registered as invalid user")

        # Verify error
        start_page.verify_sign_up_username_empty()

    def test_invalid_data_register(self, start_page, random_user):
        """
        - Pre-conditions:
            - Open start page
        - Steps:
            - Fill login, email and password fields
            - Click on Sign Up button
            - Verify Error Message
        """
        # Register using invalid data
        start_page.sign_up(username=random_user.username_value, email=random_user.email_value,
                           password=random_user.password_value)

        # Verify error
        start_page.verify_sign_up_username_invalid_data()
        start_page.verify_sign_up_email_invalid_data()
        start_page.verify_sign_up_password_invalid_data()

    def test_invalid_password_register(self, start_page, random_user):
        """
        - Pre-conditions:
            - Open start page
        - Steps:
            - Fill login, email fields
            - Fill password field with invalid data
            - Click on Sign Up button
            - Verify Error Message
        """
        # Register using invalid password data
        start_page.sign_up(username=random_user.username_value, email=random_user.email_value,
                           password=random_user.password_value)

        # Verify error
        start_page.verify_sign_up_password_invalid_data()

    def test_exist_data_register(self, start_page, random_user):
        """
        - Pre-conditions:
            - Open start page
        - Steps:
            - Fill login and email fields with exists data
            - Fill password field
            - Click on Sign Up button
            - Verify Error Message
        """

        # Register using exist login and password data
        start_page.sign_up(username=random_user.username_value, email=random_user.email_value,
                           password=random_user.password_value)

        # Verify error
        start_page.verify_sign_up_username_exists()
        start_page.verify_sign_up_email_exists()
