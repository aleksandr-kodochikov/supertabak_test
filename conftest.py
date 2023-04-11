import pytest
from pages.login_page import Login_page
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

@pytest.fixture()
def set_up():
    print('\nStart Test')
    yield
    print('\nFinish Test')

