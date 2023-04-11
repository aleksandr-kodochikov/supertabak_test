import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains

from pages.account_page import Account_page
from pages.cart_page import Cart_page
from pages.catalog_page import Catalog_page
# from pages.cart_page import Cart_page
# from pages.client_information_page import Client_information_page
# from pages.finish_page import Finish_page
from pages.login_page import Login_page
from pages.main_page import Main_page


# @pytest.mark.run(order=3)
def test_personal_account(set_up):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    g = Service('C:\\Users\\stati\\PycharmProjects\\webdriver\\chromedriver.exe')
    driver = webdriver.Chrome(options=options, service=g)

    print('Start Test Personal Account')

    login = Login_page(driver)
    login.authorization()


    ap = Account_page(driver)
    ap.personal_account()


    # print('Finish Test PA')
    # time.sleep(3)
    # driver.quit()






