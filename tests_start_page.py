"""Tests related to start page"""
import logging
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestStartPage:
    """Stores tests for start page base functionality"""

    log = logging.getLogger("[StartPage]")

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
