import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

from base.base_class import Base
from pages.main_page import Main_page


class Cart_page(Base):


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    cart_button = "//*[@id='short_cart']/a[1]"
    checkout_button = "//*[@id='basket_container']/form[2]/div[2]/div[2]/a"
    order_button = "//*[@id='order_form_content']/div[5]/div[8]/input"
    cart_name_product_1 = "//*[@id='order_form_content']/div[5]/div[6]/div[2]/table/tbody/tr/td[1]"
    cart_name_product_2 = "//*[@id='order_form_content']/div[5]/div[6]/div[2]/table/tbody/tr[1]/td[1]"

    # Getters

    def get_cart_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart_button)))

    def get_checkout_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.checkout_button)))

    def get_order_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.order_button)))



    # Actions

    def click_cart_button(self):
        # self.driver.execute_script("window.scrollTo(0, 0)")
        self.get_cart_button().click()
        print('Enter Cart')

    def click_checkout_button(self):
        self.get_checkout_button().click()
        print('Click Checkout Button')
        time.sleep(3)

    def move_to_order_button(self):
        ActionChains(self.driver).scroll_to_element(self.get_order_button()).perform()
        print('Move To Order Button')

    def save_cart_name_product_1(self):
        cart_name_product_1_text = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.cart_name_product_1)))
        global value_cart_name_product_1_text
        value_cart_name_product_1_text = cart_name_product_1_text.text
        return value_cart_name_product_1_text

    def save_cart_name_product_2(self):
        cart_name_product_2_text = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.cart_name_product_1)))
        global value_cart_name_product_2_text
        value_cart_name_product_2_text = cart_name_product_2_text.text
        return value_cart_name_product_2_text

    # Methods

    def personal_cart(self):
        self.get_current_url()
        self.click_cart_button()
        self.click_checkout_button()
        self.move_to_order_button()
        self.get_screenshot()




