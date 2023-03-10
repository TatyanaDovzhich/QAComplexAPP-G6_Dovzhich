"""Tests related to start page"""
import logging
import random
import string
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestStartPage:
    """Stores tests for start page base functionality"""

    log = logging.getLogger("[StartPage]")

    @staticmethod
    def random_num():
        """Generate random number"""
        return str(random.randint(111111, 999999))

    @staticmethod
    def random_str(length=5):
        """Generate random string"""
        return ''.join(random.choice(string.ascii_letters) for _ in range(length))

    def test_invalid_sign_in(self):
        """
        - Pre-conditions:
            - Open start page
        - Steps:
            - Fill login
            - Fill password
            - Click on SignIn button
            - Verify error
        """
        # Open start page
        driver = webdriver.Chrome(
            executable_path="F:\QALight_Python\GitHub\My Repository\QAComplexAPP-G6_Dovzhich\chromedriver")
        driver.get("https://qa-complexapp.onrender.com")
        self.log.info("Start page was opened")
        sleep(1)

        # Fill login
        login_field = driver.find_element(by=By.XPATH, value=".//input[@placeholder='Username']")
        login_field.clear()
        login_field.send_keys("test123")
        self.log.info("Login field was filled")
        sleep(1)

        # Fill password
        password_field = driver.find_element(by=By.XPATH, value=".//input[@placeholder='Password']")
        password_field.clear()
        password_field.send_keys("pwd123")
        self.log.info("Password field was filled")
        sleep(1)

        # Click on SignIn button
        sign_in_button = driver.find_element(by=By.XPATH, value=".//button[text()='Sign In']")
        sign_in_button.click()
        self.log.info("SignUp button was click")
        sleep(1)

        # Verify error
        error_message = driver.find_element(by=By.XPATH, value=".//div[@class='alert alert-danger text-center']")
        assert error_message.text == "Error"
        self.log.info("Error message was verified")
        sleep(1)

        driver.close()

    def test_empty_login(self):
        """
        - Pre-conditions:
            - Open start page
        - Steps:
            - Fill login
            - Fill password
            - Click on SignIn button
            - Verify error
        """
        # Open start page
        driver = webdriver.Chrome(
            executable_path="F:\QALight_Python\GitHub\My Repository\QAComplexAPP-G6_Dovzhich\chromedriver")
        driver.get("https://qa-complexapp.onrender.com")
        self.log.info("Start page was opened")
        sleep(1)

        # Fill login
        login_field = driver.find_element(by=By.XPATH, value=".//input[@placeholder='Username']")
        login_field.clear()
        self.log.info("Login field was filled")
        sleep(1)

        # Fill password
        password_field = driver.find_element(by=By.XPATH, value=".//input[@placeholder='Password']")
        password_field.clear()
        self.log.info("Password field was filled")
        sleep(1)

        # Click on Sign In button
        sign_in_button = driver.find_ick()
        self.log.info("SignIn button was click")
        sleep(1)

        # Verify error
        error_message = driver.find_element(by=By.XPATH, value=".//div[@class='alert alert-danger text-center']")
        assert error_message.text == "Error"
        self.log.info("Error message was verified")
        sleep(1)

        driver.close()

    def test_register(self):
        """
        - Pre-conditions:
            - Open start page
        - Steps:
            - Fill email, login and password fields
            - Click on Sign Up button
            - Verify registration is successful
        """
        # Open start page
        driver = webdriver.Chrome(
            executable_path="F:\QALight_Python\GitHub\My Repository\QAComplexAPP-G6_Dovzhich\chromedriver")
        driver.get("https://qa-complexapp.onrender.com")
        self.log.info("Open page")

        # Fill username
        username_value = f"{self.random_str()}{self.random_num()}"
        username = driver.find_element(by=By.XPATH, value=".//input[@id='username-register']")
        username.clear()
        username.send_keys(username_value)

        # Fill email
        email_value = f"{username_value}@mail.com"
        email = driver.find_element(by=By.XPATH, value=".//input[@id='email-register']")
        email.clear()
        email.send_keys(email_value)

        # Fill password
        password_value = f"{self.random_str(6)}{self.random_num()}"
        password = driver.find_element(by=By.XPATH, value=".//input[@id='password-register']")
        password.clear()
        password.send_keys(password_value)
        self.log.info("Fields were filled")
        sleep(2)

        # Click on Sign Up button
        driver.find_element(by=By.XPATH, value=".//button[@type='submit']").click()
        self.log.info("User was registered")
        sleep(1)

        # Verify register success
        hello_message = driver.find_element(by=By.XPATH, value=".//h2")
        assert username_value.lower() in hello_message.text
        assert hello_message.text == f"Hello {username_value.lower()}, your feed is empty."
        assert driver.find_element(by=By.XPATH, value=".//strong").text == username_value.lower()
        self.log.info("Registration for user '%s' was success and verified", username_value)

        driver.close()

    def test_valid_login(self):
        """
            - Pre-conditions:
            - Open start page
        - Steps:
            - Fill login
            - Fill password
            - Click on SignIn button
            - Verify login is successful
        """
        # Open start page
        driver = webdriver.Chrome(
            executable_path="F:\QALight_Python\GitHub\My Repository\QAComplexAPP-G6_Dovzhich\chromedriver")
        driver.get("https://qa-complexapp.onrender.com")
        self.log.info("Start page was opened")
        sleep(1)

        # Fill login
        login_value = f"{self.random_str()}{self.random_num()}"
        login = driver.find_element(by=By.XPATH, value=".//input[@placeholder='Username']")
        login.clear()
        login.send_keys(login_value)
        self.log.info("Login field was filled")
        sleep(1)

        # Fill password
        password_value = f"{self.random_str(6)}{self.random_num()}"
        password = driver.find_element(by=By.XPATH, value=".//input[@placeholder='Password']")
        password.clear()
        password.send_keys(password_value)
        self.log.info("Password field was filled")
        sleep(1)

        # Click on SignIn button
        sign_in_button = driver.find_element(by=By.XPATH, value=".//button[text()='Sign In']")
        sign_in_button.click()
        self.log.info("Sign In button was click")
        sleep(1)

        # Verify login success
        hello_message = driver.find_element(by=By.XPATH, value=".//h2")
        assert login_value.lower() in hello_message.text
        assert hello_message.text == f"Hello {login_value.lower()}, your feed is empty."
        assert driver.find_element(by=By.XPATH, value=".//strong").text == login_value.lower()
        self.log.info("Login for user '%s' was success and verified", login_value)

        driver.close()

    def test_invalid_login_with_empty_login_field(self):
        """
        - Pre-conditions:
            - Open start page
        - Steps:
            - Stay empty login field
            - Fill password field
            - Click on Sign In button
            - Verify Error Message
        """
        # Open start page
        driver = webdriver.Chrome(
            executable_path="F:\QALight_Python\GitHub\My Repository\QAComplexAPP-G6_Dovzhich\chromedriver")
        driver.get("https://qa-complexapp.onrender.com")
        self.log.info("Start page was opened")
        sleep(1)

        # Stay empty login field
        login = driver.find_element(by=By.XPATH, value=".//input[@placeholder='Username']")
        login.clear()
        self.log.info("Login field remains empty")
        sleep(1)

        # Fill password field
        password_value = f"{self.random_str(6)}{self.random_num()}"
        password = driver.find_element(by=By.XPATH, value=".//input[@placeholder='Password']")
        password.clear()
        password.send_keys(password_value)
        self.log.info("Password field was filled")
        sleep(1)

        # Click on Sign In button
        sign_in_button = driver.find_element(by=By.XPATH, value=".//button[text()='Sign In']")
        sign_in_button.click()
        self.log.info("Sign In button was click")
        sleep(1)

        # Verify Error Message
        error_message = driver.find_element(by=By.XPATH, value=".//div[@class='alert alert-danger text-center']")
        assert error_message.text == "Error"
        self.log.info("Error message was verified")
        sleep(1)

        driver.close()

    def test_invalid_login_with_empty_password_field(self):
        """
        - Pre-conditions:
            - Open start page
        - Steps:
            - Fill login field
            - Stay empty password field
            - Click on Sign In button
            - Verify Error Message
        """
        # Open start page
        driver = webdriver.Chrome(
            executable_path="F:\QALight_Python\GitHub\My Repository\QAComplexAPP-G6_Dovzhich\chromedriver")
        driver.get("https://qa-complexapp.onrender.com")
        self.log.info("Start page was opened")
        sleep(1)

        # Fill login field
        login_value = f"{self.random_str()}{self.random_num()}"
        login = driver.find_element(by=By.XPATH, value=".//input[@placeholder='Username']")
        login.clear()
        login.send_keys(login_value)
        self.log.info("Login field was filled")
        sleep(1)

        # Stay empty password field
        password = driver.find_element(by=By.XPATH, value=".//input[@placeholder='Password']")
        password.clear()
        self.log.info("Password field remains empty")
        sleep(1)

        # Click on Sign In button
        sign_in_button = driver.find_element(by=By.XPATH, value=".//button[text()='Sign In']")
        sign_in_button.click()
        self.log.info("Sign In button was click")
        sleep(1)

        # Verify Error Message
        error_message = driver.find_element(by=By.XPATH, value=".//div[@class='alert alert-danger text-center']")
        assert error_message.text == "Error"
        self.log.info("Error message was verified")
        sleep(1)

        driver.close()

    def test_invalid_login_with_invalid_username(self):
        """
        - Pre-conditions:
            - Open start page
        - Steps:
            - Fill login field with invalid data
            - Fill password field
            - Click on Sign In button
            - Verify Error Message
        """
        # Open start page
        driver = webdriver.Chrome(executable_path="F:\QALight_Python\pythonProject4\chromedriver")
        driver.get("https://qa-complexapp.onrender.com")
        self.log.info("Start page was opened")
        sleep(1)

        # Fill login field with invalid data
        login_field = driver.find_element(by=By.XPATH, value=".//input[@placeholder='Username']")
        login_field.clear()
        login_field.send_keys("test123")
        self.log.info("Login field was filled")
        sleep(1)

        # Fill password field
        password_value = f"{self.random_str(6)}{self.random_num()}"
        password = driver.find_element(by=By.XPATH, value=".//input[@placeholder='Password']")
        password.clear()
        password.send_keys(password_value)
        self.log.info("Password field was filled")
        sleep(1)

        # Click on Sign In button
        sign_in_button = driver.find_element(by=By.XPATH, value=".//button[text()='Sign In']")
        sign_in_button.click()
        self.log.info("Sign In button was click")
        sleep(1)

        # Verify Error Message
        error_message = driver.find_element(by=By.XPATH,
                                            value=".//div[@class='alert alert-danger text-center']")
        assert error_message.text == "Error"
        self.log.info("Error message was verified")
        sleep(1)

        driver.close()

    def test_invalid_login_with_invalid_password(self):
        """
        - Pre-conditions:
            - Open start page
        - Steps:
            - Fill login field
            - Fill password field with invalid data
            - Click on Sign In button
            - Verify Error Message
        """
        # Open start page
        driver = webdriver.Chrome(executable_path="F:\QALight_Python\pythonProject4\chromedriver")
        driver.get("https://qa-complexapp.onrender.com")
        self.log.info("Start page was opened")
        sleep(1)

        # Fill login field
        login_value = f"{self.random_str()}{self.random_num()}"
        login = driver.find_element(by=By.XPATH, value=".//input[@placeholder='Username']")
        login.clear()
        login.send_keys(login_value)
        self.log.info("Login field was filled")

        # Fill password field with invalid data
        password = driver.find_element(by=By.XPATH, value=".//input[@placeholder='Password']")
        password.clear()
        password.send_keys("pwd123")
        self.log.info("Password field was filled")
        sleep(1)

        # Click on Sign In button
        sign_in_button = driver.find_element(by=By.XPATH, value=".//button[text()='Sign In']")
        sign_in_button.click()
        self.log.info("Sign In button was click")
        sleep(1)

        # Verify Error Message
        error_message = driver.find_element(by=By.XPATH, value=".//div[@class='alert alert-danger text-center']")
        assert error_message.text == "Error"
        self.log.info("Error message was verified")
        sleep(1)

        driver.close()
