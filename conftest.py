import pytest
from selenium import webdriver

from constants.base import BaseConstants
from pages.create_post_page import CreatePostPage
from pages.hello_page import HelloPage
from pages.post_page import PostPage
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


@pytest.fixture()
def hello_page(driver):
    """Creates hello page object"""
    driver.get(BaseConstants.URL)
    driver.implicity_wait(1)
    return HelloPage(driver)


@pytest.fixture()
def create_post_page(driver):
    """Creates create_post page object"""
    driver.get(BaseConstants.URL_CREATE_POST)
    driver.implicity_wait(1)
    return CreatePostPage(driver)


@pytest.fixture()
def post_page(driver):
    """Creates post page object"""
    driver.get(BaseConstants.URL_POST)
    driver.implicity_wait(1)
    return PostPage
