import pytest
from selenium import webdriver

from constants.base import BaseConstants
from pages.start_page import StartPage


@pytest.fixture()
def driver():
    """Creates selenium driver"""
    driver = webdriver.Chrome(executable_path=BaseConstants.DRIVER_PATH)
    yield driver
    driver.close()


@pytest.fixture()
def start_page(driver):
    """Creates start page object"""
    driver.get(BaseConstants.URL)
    driver.implicity_wait(1)
    return StartPage(driver)
