"""Tests related to start page"""
import logging

from pages.utils import random_num, random_str


class TestStartPage:
    """Stores tests for start page base functionality"""

    log = logging.getLogger("[TestStartPage]")

    def test_valid_login(self, start_page):
        """
            - Pre-conditions:
            - Open start page
        - Steps:
            - Fill login
            - Fill password
            - Click on SignIn button
            - Verify login is successful
        """
        # Prepare test data
        username_value = f"{random_str()}{random_num()}"
        password_value = f"{random_str(6)}{random_num()}"

        # Login as valid user
        hello_page = start_page.sign_in(username=username_value, password=password_value)
        self.log.info("User logged in")

        # Verify login success
        hello_page.verify_sign_in_message(username=username_value)
        self.log.info("Registration for user '%s' was success and verified", username_value)

    def test_invalid_login(self, start_page):
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
        start_page.sign_in("test123", "pwd123")
        self.log.info("Logged in as invalid user")

        # Verify error
        start_page.verify_sign_in_error()
        self.log.info("Error message was verified")

    def test_empty_login(self, start_page):
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
        start_page.sign_in("", "")
        self.log.info("Logged in as invalid user")

        # Verify error
        start_page.verify_sign_in_error()
        self.log.info("Error message was verified")

    def test_invalid_login_with_empty_login_field(self, start_page):
        """
        - Pre-conditions:
            - Open start page
        - Steps:
            - Stay empty login field
            - Fill password field
            - Click on Sign In button
            - Verify Error Message
        """
        # Prepare test data
        password_value = f"{random_str(6)}{random_num()}"

        # Login as invalid user
        start_page.sign_in("", password=password_value)
        self.log.info("Logged in as invalid user")

        # Verify error
        start_page.verify_sign_in_error()
        self.log.info("Error message was verified")

    def test_invalid_login_with_empty_password_field(self, start_page):
        """
        - Pre-conditions:
            - Open start page
        - Steps:
            - Fill login field
            - Stay empty password field
            - Click on Sign In button
            - Verify Error Message
        """
        # Prepare test data
        username_value = f"{random_str()}{random_num()}"

        # Login as invalid user
        start_page.sign_in(username=username_value, password="")
        self.log.info("Logged in as invalid user")

        # Verify error
        start_page.verify_sign_in_error()
        self.log.info("Error message was verified")

    def test_invalid_login_with_invalid_username(self, start_page):
        """
        - Pre-conditions:
            - Open start page
        - Steps:
            - Fill login field with invalid data
            - Fill password field
            - Click on Sign In button
            - Verify Error Message
        """
        # Prepare test data
        password_value = f"{random_str(6)}{random_num()}"

        # Login as invalid user
        start_page.sign_in("test123", password=password_value)
        self.log.info("Logged in as invalid user")

        # Verify error
        start_page.verify_sign_in_error()
        self.log.info("Error message was verified")

    def test_invalid_login_with_invalid_password(self, start_page):
        """
        - Pre-conditions:
            - Open start page
        - Steps:
            - Fill login field
            - Fill password field with invalid data
            - Click on Sign In button
            - Verify Error Message
        """
        # Prepare test data
        username_value = f"{random_str()}{random_num()}"

        # Login as invalid user
        start_page.sign_in(username=username_value, password="pass123")
        self.log.info("Logged in as invalid user")

        # Verify error
        start_page.verify_sign_in_error()
        self.log.info("Error message was verified")

    def test_register(self, start_page):
        """
        - Pre-conditions:
            - Open start page
        - Steps:
            - Fill login, email and password fields
            - Click on Sign Up button
            - Verify registration is successful
        """
        # Prepare test data
        username_value = f"{random_str()}{random_num()}"
        email_value = f"{username_value}@mail.com"
        password_value = f"{random_str(6)}{random_num()}"

        # Fill email, login and password fields
        hello_page = start_page.sign_up(username=username_value, email=email_value, password=password_value)
        self.log.info("User was registered")

        # Verify register success
        hello_page.verify_sign_up_message(username=username_value)
        self.log.info("Registration for user '%s' was success and verified", username_value)

    def test_empty_fields_register(self, start_page):
        """
        - Pre-conditions:
            - Open start page
        - Steps:
            - Stay empty login, email and password fields
            - Click on Sign Up button
            - Verify Error Message
        """
        # Register using empty fields
        start_page.sign_up("", "", "")
        self.log.info("Registered as invalid user")

        # Verify error
        start_page.verify_sign_up_username_empty()
        start_page.verify_sign_up_email_empty()
        start_page.verify_sign_up_password_empty()
        self.log.info("Error messages were verified")

    def test_empty_username_register(self, start_page):
        """
        - Pre-conditions:
            - Open start page
        - Steps:
            - Stay empty username field
            - Fill email and password fields
            - Click on Sign Up button
            - Verify Error Message
        """
        # Prepare test data
        username_value = ""
        email_value = f"{username_value}@mail.com"
        password_value = f"{random_str(6)}{random_num()}"

        # Register using empty username
        start_page.sign_up(username=username_value, email=email_value, password=password_value)
        self.log.info("Registered as invalid user")

        # Verify error
        start_page.verify_sign_up_username_empty()
        self.log.info("Error message was verified")

    def test_invalid_data_register(self, start_page):
        """
        - Pre-conditions:
            - Open start page
        - Steps:
            - Fill login, email and password fields
            - Click on Sign Up button
            - Verify Error Message
        """
        # Register using invalid data
        start_page.sign_up("test_123", "email", "123f")
        self.log.info("Registered as invalid user")

        # Verify error
        start_page.verify_sign_up_username_invalid_data()
        start_page.verify_sign_up_email_invalid_data()
        start_page.verify_sign_up_password_invalid_data()
        self.log.info("Error messages were verified")

    def test_invalid_password_register(self, start_page):
        """
        - Pre-conditions:
            - Open start page
        - Steps:
            - Fill login, email fields
            - Fill password field with invalid data
            - Click on Sign Up button
            - Verify Error Message
        """
        # Prepare test data
        username_value = f"{random_str()}{random_num()}"
        email_value = f"{username_value}@mail.com"
        password_value = "pass1"

        # Register using invalid password data
        start_page.sign_up(username=username_value, email=email_value, password=password_value)
        self.log.info("Registered as invalid user")

        # Verify error
        start_page.verify_sign_up_password_invalid_data()
        self.log.info("Error message was verified")

    def test_exist_data_register(self, start_page):
        """
        - Pre-conditions:
            - Open start page
        - Steps:
            - Fill login and email fields with exists data
            - Fill password field
            - Click on Sign Up button
            - Verify Error Message
        """
        # Prepare test data
        username_value = "exist"
        email_value = f"{username_value}@mail.com"
        password_value = f"{random_str(6)}{random_num()}"

        # Register using exist login and password data
        start_page.sign_up(username=username_value, email=email_value, password=password_value)
        self.log.info("Registered as invalid user")

        # Verify error
        start_page.verify_sign_up_username_exists()
        start_page.verify_sign_up_email_exists()
        self.log.info("Error messages were verified")
