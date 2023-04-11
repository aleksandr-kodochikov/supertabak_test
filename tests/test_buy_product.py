import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains

from base.base_class import Base
from pages.account_page import Account_page
from pages.cart_page import Cart_page
from pages.catalog_page import Catalog_page
from pages.enter_page import Enter_page
# from pages.cart_page import Cart_page
# from pages.client_information_page import Client_information_page
# from pages.finish_page import Finish_page
from pages.login_page import Login_page
from pages.main_page import Main_page


# from pages.main_page import Main_page
# from pages.payment_page import Payment_page

def test_age_control(set_up):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    g = Service('C:\\Users\\stati\\PycharmProjects\\webdriver\\chromedriver.exe')
    driver = webdriver.Chrome(options=options, service=g)

    print('Start Test Age Control')

    age = Enter_page(driver)
    age.age_control()

    print('Finish Test Age Control')
    time.sleep(3)
    driver.quit()


# @pytest.mark.run(order=3)
def test_buy_product_1(set_up):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    g = Service('C:\\Users\\stati\\PycharmProjects\\webdriver\\chromedriver.exe')
    driver = webdriver.Chrome(options=options, service=g)

    print('Start Test 1')

    login = Login_page(driver)
    login.authorization()

    ctp = Catalog_page(driver)
    ctp.select_products_1()

    item_ctp_1 = Catalog_page(driver)
    item_ctp_1_text = item_ctp_1.save_name_product_1()

    cp = Cart_page(driver)
    cp.personal_cart()

    item_cp_1 = Cart_page(driver)
    item_cp_1_text = item_cp_1.save_cart_name_product_1()

    check_item = Base(driver)
    check_item.assert_item(item_ctp_1_text, item_cp_1_text)

    print('Finish Test 1')
    time.sleep(5)
    driver.quit()

# @pytest.mark.run(order=1)
def test_buy_product_2(set_up):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    g = Service('C:\\Users\\stati\\PycharmProjects\\webdriver\\chromedriver.exe')
    driver = webdriver.Chrome(options=options, service=g)

    print('Start Test 2')

    login = Login_page(driver)
    login.authorization()

    mp = Main_page(driver)
    mp.select_products_2()

    item_mp_2 = Main_page(driver)
    item_mp_2_text = item_mp_2.save_name_product_2()

    cp = Cart_page(driver)
    cp.personal_cart()

    item_cp_2 = Cart_page(driver)
    item_cp_2_text = item_cp_2.save_cart_name_product_2()

    check_item = Base(driver)
    check_item.assert_item(item_mp_2_text, item_cp_2_text)

    print('Finish Test 2')
    time.sleep(5)
    driver.quit()






